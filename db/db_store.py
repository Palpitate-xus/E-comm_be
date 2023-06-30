from models.storemodel.product import Product
from models.usermodel.orders import Orders
from .database import execute_query

def productlist():
    # 查询所有商品
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id"
    result = execute_query(query)
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

# def send_order(supply_order:Supply_order):
#     #将订单数据加入至数据库中
#     sql="INSERT INTO Supply_order(supplyorder_id, supplier_id,product_id,quantity,storage_time) VALUES (%s,%s,%s,%s,%s)"
#     storage_time=datetime.now()
#     supplyorder_id=str(uuid.uuid4())
#     result=execute_query(sql,(supplyorder_id,supply_order.supplier_id, supply_order.product_id, supply_order.stock_quantity, storage_time))