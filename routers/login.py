from fastapi import APIRouter, HTTPException
from db.database import login
from utils.auth import generate_token
from models.user import User
router = APIRouter()

@router.post("/api/users/login/")
async def login(user: User):

    result = login(user)

    if result is None:
        # 用户名或密码不匹配，返回错误响应
        raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        # 生成JWT令牌
        token = generate_token(user.username)

        # 返回包含令牌的成功响应
        return {"code": 200, "message": "Login successful", "data": {"token": token}}
