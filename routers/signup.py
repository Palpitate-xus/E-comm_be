from fastapi import APIRouter
from models.user import User
from db import database

router = APIRouter()


@router.post("/api/users/register/")
def register_user(user: User):
    # 在数据库中插入用户信息
    database.create_user(user)

    return {"code": 200, "message": "User account created successfully", "data": {}}


