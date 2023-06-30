

from models.usermodel.user import User
from models.usermodel.orders import Orders
import uuid
from models.usermodel.create_order import CreateOrder
from .database import execute_query
from utils.auth import decode_token

def create_order(createorder: CreateOrder, token):
    # 生成订单ID
    order_id = str(uuid.uuid4())

    total_amount = 0.0
    supplier_order_ids = {}  # 用于存储每个供应商的订单ID

    # 插入用户订单信息
    sql_insert_order = "INSERT INTO Orders (order_id, user_id, order_status, total_amount, order_time, payment_status, shipping_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(sql_insert_order, (order_id, decode_token(token,"your_secret_key")['userid'], createorder.order_status, total_amount, createorder.order_time,
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
            execute_query(sql_insert_supplier_order, (supplier_order_id, supplier_id, createorder.order_status, createorder.order_time))

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

    return 1


def remove_order(order: Orders):
    sql = "DELETE FROM Order_detail WHERE order_id = %s"
    execute_query(sql, (order.order_id))
    sql = "DELETE FROM Orders WHERE order_id = %s"
    execute_query(sql, (order.order_id))

def pay_order(order: Orders):
    sql = "UPDATE Orders SET payment_status = 'Paid' WHERE order_id = %s AND user_id = %s"
    execute_query(sql, (order.order_id, order.user_id))


def get_order_detail(order: Orders):
    sql = "SELECT * FROM Order_detail WHERE order_id = %s"
    results = execute_query(sql, (order.order_id))
    return results

def get_order_list(token):
    sql = "SELECT * FROM Orders WHERE user_id = %s"
    results = execute_query(sql, (decode_token(token,"your_secret_key")['userid']))
    return results