from fastapi import APIRouter
from models.user import User
from db import db_user

router = APIRouter()


@router.post("/api/users/reset_password/")
def reset_password(user: User):
    # 在数据库中重制密码
    db_user.reset_password(user)

    return {"code": 200, "message": "Password reset successful", "data": {}}