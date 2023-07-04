
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori,association_rules
from models.usermodel.orders import Orders
from models.usermodel.order_details import OrderDetail
import uuid
from models.usermodel.create_order import CreateOrder
from .database import execute_query,get_connection
from utils.auth import decode_token
from datetime import datetime
def create_order(createorder: CreateOrder, token):
    # 生成订单ID
    order_id = str(uuid.uuid4())

    total_amount = 0.0
    supplier_order_ids = {}  # 用于存储每个供应商的订单ID

    # 插入用户订单信息
    sql_insert_order = "INSERT INTO Orders (order_id, user_id, order_status, total_amount, order_time, payment_status, shipping_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(sql_insert_order, (order_id, decode_token(token,"your_secret_key")['userid'], createorder.order_status, total_amount, datetime.now(),
                                      createorder.payment_status, createorder.shipping_address))

    for order_detail in createorder.order_details:
        # 查询库存数量并找到匹配的供应商ID
        sql_check_inventory = "SELECT stock_quantity, supplier_id FROM Inventory WHERE product_id = %s"
        result = execute_query(sql_check_inventory, (order_detail.product_id))
        stock_quantity, supplier_id = result[0]  # 获取库存数量和供应商ID

        if stock_quantity < order_detail.quantity:
            # 库存不足，删除已插入的订单信息
            sql_delete_order = "DELETE FROM Orders WHERE order_id = %s"
            execute_query(sql_delete_order, (order_id,))
            return 0

        # 计算商品总价格
        total_amount += order_detail.quantity * order_detail.product_price

        # 更新库存数量
        updated_stock_quantity = stock_quantity - order_detail.quantity
        sql_update_inventory = "UPDATE Inventory SET stock_quantity = %s WHERE product_id = %s"
        execute_query(sql_update_inventory, (updated_stock_quantity, order_detail.product_id))

        # 创建供应商订单并记录供应商订单ID
        if supplier_id not in supplier_order_ids:
            supplier_order_id = str(uuid.uuid4())
            supplier_order_ids[supplier_id] = supplier_order_id

            sql_insert_supplier_order = "INSERT INTO Supply_order (supplyorder_id, supplier_id, order_status, order_time) VALUES (%s, %s, %s, %s)"
            execute_query(sql_insert_supplier_order, (supplier_order_id, supplier_id, createorder.order_status, datetime.now()))

        supplier_order_id = supplier_order_ids[supplier_id]

        # 填写供应商订单详情表
        sql_insert_supplier_order_detail = "INSERT INTO Supply_orderdetail (supplyorder_id, product_id, quantity, order_id) VALUES (%s, %s, %s, %s)"
        execute_query(sql_insert_supplier_order_detail, (supplier_order_id, order_detail.product_id, order_detail.quantity, order_id))

    # 更新用户订单的总金额
    sql_update_order_total_amount = "UPDATE Orders SET total_amount = %s WHERE order_id = %s"
    execute_query(sql_update_order_total_amount, (total_amount, order_id))

    for order_detail in createorder.order_details:
        sql_insert_order_detail = "INSERT INTO Order_detail (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)"
        execute_query(sql_insert_order_detail, (order_id, order_detail.product_id, order_detail.quantity, order_detail.product_price))

    sql_clear_cart = "DELETE FROM Shopping_cart WHERE user_id = %s"
    execute_query(sql_clear_cart, (decode_token(token,"your_secret_key")['userid']))

    return order_id


def remove_order(order: Orders):
    sql = "DELETE FROM Order_detail WHERE order_id = %s"
    execute_query(sql, (order.order_id))
    sql = "DELETE FROM Orders WHERE order_id = %s"
    execute_query(sql, (order.order_id))

def pay_order(order_id):
    sql = "UPDATE Orders SET payment_status = 'Paid' WHERE order_id = %s"
    execute_query(sql, (order_id))
    sql = """
            UPDATE Supply_order
            INNER JOIN Supply_orderdetail ON Supply_order.supplyorder_id = Supply_orderdetail.supplyorder_id
            SET Supply_order.order_status = 'Has paid'
            WHERE Supply_orderdetail.order_id = %s
        """
    execute_query(sql, (order_id))


def get_order_detail(result):
    sql = """
        SELECT od.*, p.product_name
        FROM Order_detail od
        INNER JOIN Product p ON od.product_id = p.product_id
        WHERE od.order_id = %s
    """
    results = execute_query(sql, (result))
    return results

def get_order_detail1(orderdetail:OrderDetail):
    sql = """
        SELECT od.*, p.product_name
        FROM Order_detail od
        INNER JOIN Product p ON od.product_id = p.product_id
        WHERE od.order_id = %s
    """
    results = execute_query(sql, (orderdetail.order_id))
    return results


def get_order_list(token):
    sql = "SELECT * FROM Orders WHERE user_id = %s"
    results = execute_query(sql, (decode_token(token,"your_secret_key")['userid']))
    return results



def get_recomm(token):
    query = """SELECT Order_detail.order_id, Order_detail.product_id
    FROM Order_detail
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    # Create a DataFrame from the rows and column names
    df = pd.DataFrame(rows, columns=columns)

    transactions = df.groupby('order_id')['product_id'].apply(list).values.tolist()
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df_encoded, min_support=0.2, use_colnames=True)
    rules = association_rules(frequent_itemsets)
    filtered_rules = rules[(rules['confidence'] > 0.5) & (rules['lift'] > 1)]
    sql = """
    SELECT Order_detail.product_id
            FROM Order_detail
            INNER JOIN Orders ON Orders.order_id = Order_detail.order_id
            WHERE Orders.user_id = %s
    """
    his = []
    result = execute_query(sql, (decode_token(token,"your_secret_key")['userid']))
    for i in result:
        his.append(i[0])
    user_purchases = his
    # 创建一个空的推荐列表
    recommendations = []
    for _, row in filtered_rules.iterrows():
        antecedents = row['antecedents']
        consequents = row['consequents']
        # 检查antecedents是否为购买记录的子集
        if set(antecedents).issubset(set(user_purchases)):
            # 将consequents添加到推荐列表中
            recommendations.extend(consequents)
    # 去除重复的推荐商品
    recommendations = list(set(recommendations))
    # 打印推荐的商品列表
    print(recommendations)
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id WHERE p.product_status = 'active' and p.product_id IN ({})".format(",".join(map(str, recommendations)))
    result = execute_query(query)
    return result