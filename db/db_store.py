from models.user import User
from .database import execute_query,get_connection,close_connection

def productlist():
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT * FROM Product"
    result = execute_query(query)
    # print(result)
    return result