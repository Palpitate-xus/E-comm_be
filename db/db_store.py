from models.product import Product
from .database import execute_query

def productlist():
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT * FROM Product"
    result = execute_query(query)
    # print(result)
    return result

def searchproduct(product: Product):
    # Query the database to search for products with matching names
    query = "SELECT * FROM Product WHERE product_name LIKE %s"
    result = execute_query(query,('%'+product.product_name+'%'))
    return result