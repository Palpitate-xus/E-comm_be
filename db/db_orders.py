

from models.user import User
from models.orders import Orders
import uuid
from models.create_order import CreateOrder
from .database import execute_query


def create_order(createorder: CreateOrder):
    # 生成订单ID
    order_id = str(uuid.uuid4())

    total_amount = 0.0
    for order_detail in createorder.order_details:
        # 计算商品总价格
        total_amount += order_detail.quantity * order_detail.unit_price

    # 插入订单信息
    sql = "INSERT INTO Orders (order_id, user_id, order_status, total_amount, order_time, payment_status, shipping_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(sql, (order_id, createorder.user_id, createorder.order_status, total_amount, createorder.order_time,
                        createorder.payment_status, createorder.shipping_address))

    for order_detail in createorder.order_details:
        sql2 = "INSERT INTO Order_detail (order_id, product_id, quantity, unit_price) VALUES (%s, %s, %s, %s)"
        execute_query(sql2, (order_id, order_detail.product_id, order_detail.quantity, order_detail.unit_price))

    sql_clear_cart = "DELETE FROM Shopping_cart WHERE user_id = %s"
    execute_query(sql_clear_cart, (createorder.user_id))



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

def get_order_list(user: User):
    sql = "SELECT * FROM Orders WHERE user_id = %s"
    results = execute_query(sql, (user.user_id))
    return results