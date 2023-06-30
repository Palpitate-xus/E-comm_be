from fastapi import APIRouter
from models.usermodel.user import User
from db import database

router = APIRouter()

@router.post("/users/{user_id}/update")
def update_user(user_id: int, user: User):
    # 根据用户ID和传入的用户信息进行用户信息的更新操作
    connection = database.get_connection()
    try:
        with connection.cursor() as cursor:
            # 执行更新用户信息的SQL语句，假设users表为存储用户信息的表
            update_query = "UPDATE users SET username=%s, password=%s, usertype=%s WHERE id=%s"
            cursor.execute(update_query, (user.username, user.password, user.type, user_id))
            connection.commit()

            # 返回成功消息
            return {"message": "User information updated successfully"}
    finally:
        database.close_connection(connection)