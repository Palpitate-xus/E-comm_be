from models.orders import Orders
from .database import execute_query

def create_order(order: Orders):
    sql = "INSERT INTO Orders (order_id, user_id, order_status, total_amount, order_time, payment_status, payment_method, shipping_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    execute_query(sql, (order.order_id, order.user_id, order.order_status, order.total_amount, order.order_time, order.payment_status, order.payment_method, order.shipping_address))


def remove_order(order: Orders):
    sql = "DELETE FROM Orders WHERE order_id = %s AND user_id = %s"
    execute_query(sql, (order.order_id, order.user_id))