from fastapi import APIRouter, HTTPException
from db.database import execute_query
from utils.auth import generate_token
from models.user import User
router = APIRouter()

@router.post("/login/")
async def login(user: User):
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT * FROM users WHERE username=%s AND password=%s AND type=%s"
    result = execute_query(query, (user.username, user.password, user.type))

    if result is None:
        # 用户名或密码不匹配，返回错误响应
        raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        # 生成JWT令牌
        token = generate_token(user.username)

        # 返回包含令牌的成功响应
        return {"token": token}
