from fastapi import APIRouter, HTTPException
from db import db_user
from utils.auth import generate_token
from models.usermodel.user import User
router = APIRouter()

@router.post("/api/users/login/")
async def login(user: User):

    result = db_user.login(user)
    if len(result) == 0:
        # 邮箱或密码不匹配，返回错误响应
        return {"code": 403, "message": "Invalid email or password", "data":{}}
    else:
        # 生成JWT令牌
        token = generate_token(result[0][0])
        if user.user_type == 'customer':
            return {"code": 200, "message": "Login successful", "data": {"token": token}}
        # 返回包含令牌的成功响应
        else:
            return {"code": 200, "message": "Login successful", "data": {"Authorization": token}}
