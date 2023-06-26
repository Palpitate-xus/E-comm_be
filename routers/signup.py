from fastapi import APIRouter
from models.user import User
from db import database

router = APIRouter()


@router.post("/singup/")
def register_user(user: User):
    # 在数据库中插入用户信息
    connection = database.get_connection()
    try:
        with connection.cursor() as cursor:
            # 执行插入操作
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (user.username, user.password))
        connection.commit()
    finally:
        database.close_connection(connection)

    return {"message": "User registered successfully"}


