import pymysql

# 数据库连接信息
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456789',
    'database': 'E-commerce_platform',
}
#建立连接
def get_connection():
    return pymysql.connect(**DB_CONFIG)

#关闭连接
def close_connection(connection):
    connection.close()

#执行sql语句
def execute_query(query, params=None):
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchone()
    close_connection(connection)
    return result
