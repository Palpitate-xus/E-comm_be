from models.storemodel.product import Product
from models.usermodel.orders import Orders
from .database import execute_query

def productlist():
    # 查询所有状态为 "active" 的商品
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id WHERE p.product_status = 'active'"
    result = execute_query(query)
    return result

def productlist1():
    # 查询所有商品
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id"
    result = execute_query(query)
    return result

def productlist2(x):
    query = "SELECT supplier_id FROM Supplier WHERE user_id = %s"
    result = execute_query(query, x)
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id WHERE i.supplier_id = %s "
    result = execute_query(query,result[0][0])
    return result

def orderlist():
    # 查询所有订单
    sql = "SELECT * FROM Orders"
    results = execute_query(sql)
    return results

def searchproduct(product: Product):
    # Query the database to search for products with matching names
    query = "SELECT p.*, i.stock_quantity FROM Product p INNER JOIN Inventory i ON p.product_id = i.product_id WHERE product_name LIKE %s"
    result = execute_query(query,('%'+product.product_name+'%'))
    return result


def offshelf(product: Product):
    # Update the product status to "offshelf" in the Product table
    query = "UPDATE Product SET product_status = 'offshelf' WHERE product_id = %s"
    execute_query(query, (product.product_id))

def onshelf(product: Product):
    # Update the product status to "offshelf" in the Product table
    query = "UPDATE Product SET product_status = 'active' WHERE product_id = %s"
    execute_query(query, (product.product_id))