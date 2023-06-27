from fastapi import APIRouter
from models.user import User
from db import db_user

router = APIRouter()


@router.post("/api/users/register/")
def register_user(user: User):
    # 在数据库中插入用户信息
    db_user.create_user(user)

    return {"code": 200, "message": "User account created successfully", "data": {}}


