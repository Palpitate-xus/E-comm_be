import pymysql
from .config import DB_CONFIG
#建立连接
def get_connection():
    return pymysql.connect(**DB_CONFIG)

#关闭连接
def close_connection(connection):
    connection.close()


#执行sql语句
def execute_query(query, params=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
    finally:
        close_connection(connection)
    return result

