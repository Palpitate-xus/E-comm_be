from models.product import Product
from models.orders import Orders
from .database import execute_query

def productlist():
    # 查询所有商品
    query = "SELECT * FROM Product"
    result = execute_query(query)
    # print(result)
    return result

def orderlist():
    # 查询所有订单
    sql = "SELECT * FROM Orders"
    results = execute_query(sql)
    return results

def searchproduct(product: Product):
    # Query the database to search for products with matching names
    query = "SELECT * FROM Product WHERE product_name LIKE %s"
    result = execute_query(query,('%'+product.product_name+'%'))
    return result

def accept_order(order: Orders):
    sql = "UPDATE Orders SET order_status = 'Accepted' WHERE order_id = %s AND order_status = 'Pending'"
    execute_query(sql, (order.order_id))

def reject_order(order: Orders):
    sql = "UPDATE Orders SET order_status = 'Rejected' WHERE order_id = %s AND order_status = 'Pending'"
    execute_query(sql, (order.order_id))