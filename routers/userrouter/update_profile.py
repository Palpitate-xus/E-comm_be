from fastapi import APIRouter
from models.user import User
from db import db_user

router = APIRouter()


@router.post("/api/users/update_profile/")
def reset_password(user: User):
    # 在数据库中更新用户信息
    db_user.edit_user_info(user)

    return {"code": 200, "message":   "Profile updated successfully", "data": {}}
