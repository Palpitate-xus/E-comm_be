from models.user import User
from models.order_details import OrderDetail
from db.database import execute_query,get_connection,close_connection

#登陆,返回user_id
def login(user: User):
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT user_id FROM User WHERE username=%s AND password=%s AND user_type=%s"
    result = execute_query(query, (user.username, user.password, user.user_type))
    return result
#创建新用户
def create_user(user: User):
    sql = "INSERT INTO User (username, password, email, user_type, registration_date, user_status) VALUES (%s, %s, %s, %s, %s, %s)"
    execute_query(sql, (user.username, user.password, user.email, user.user_type, user.registration_date, user.user_status))
#修改密码
def reset_password(user: User):
    sql = "UPDATE User SET password = %s WHERE email = %s"
    execute_query(sql, (user.password, user.email))
#修改个人信息
def edit_user_info(user: User):
    sql = "UPDATE User SET email = %s, username = %s, password = %s WHERE user_id = %s"
    execute_query(sql, (user.email, user.username, user.password, user.user_id))




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