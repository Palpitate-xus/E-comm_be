from fastapi import APIRouter
from models.usermodel.user import User
from db import db_user

router = APIRouter()


@router.post("/api/users/reset_password/")
def reset_password(user: User):
    # 在数据库中重制密码
    result = db_user.reset_password(user)
    if result == 0:
        return {"code": 404, "message": "Email address didn't exist", "data": {}}
    return {"code": 200, "message": "Password reset successful", "data": {}}