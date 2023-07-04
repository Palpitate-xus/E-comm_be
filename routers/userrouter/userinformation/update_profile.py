from fastapi import APIRouter
from models.usermodel.user import User
from db import db_user
from fastapi import Request
router = APIRouter()


@router.post("/api/users/update_profile/")
def reset_password(user: User, request: Request):
    # 获取前端传递的token
    token = request.headers.get("Authorization")
    # 更新用户信息
    db_user.edit_user_info(user,token)

    return {"code": 200, "message":   "Profile updated successfully", "data": {}}
