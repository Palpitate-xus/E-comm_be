import pymysql
from models.user import User
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
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
    finally:
        close_connection(connection)
    return result

#登陆
def login(user: User):
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT * FROM User WHERE username=%s AND password=%s AND usertype=%s"
    result = execute_query(query, (user.username, user.password, user.usertype))
    return result

#创建新用户
def create_user(user: User):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO User (username, password, email, user_type, registration_date, user_status) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user.username, user.password, user.email, user.user_type, user.registration_date, user.user_status))
        connection.commit()
    finally:
        close_connection(connection)

# 根据id删除用户
def delete_user(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM User WHERE id = %s"
            cursor.execute(sql, (user_id,))
            connection.commit()
            return cursor.rowcount > 0
    finally:
        close_connection(connection)

# 根据用户名模糊查找
def search_users(user: User):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM User WHERE username LIKE %s"
            cursor.execute(sql, (f"%{user.username}%",))
            result = cursor.fetchall()
            users = [User(username=row['username'], password=row['password'], usertype=row['usertype']) for row in result]
            return users
    finally:
        close_connection(connection)