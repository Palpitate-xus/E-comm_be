from fastapi import APIRouter
from models.user import User
from db import database

router = APIRouter()


@router.post("/createuser/")
def register_user(user: User):
    # 在数据库中插入用户信息
    database.create_user(user)

    return {"message": "User created successfully"}


@router.post("/deleteuser/")
def register_user(user: User):
    # 在数据库中删除用户信息
    database.delete_user(user)

    return {"message": "User deleted successfully"}


@router.get("/findusers")
def get_users(user: User):
    users = database.search_users(user)
    return {"users": users}
