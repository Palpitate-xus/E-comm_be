from fastapi import APIRouter, HTTPException
from db.database import execute_query
from utils.auth import generate_token

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    # 查询数据库中是否存在匹配的用户名和密码
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    result = execute_query(query, (username, password))

    if result is None:
        # 用户名或密码不匹配，返回错误响应
        raise HTTPException(status_code=401, detail="Invalid username or password")
    else:
        # 生成JWT令牌
        token = generate_token(username)

        # 返回包含令牌的成功响应
        return {"token": token}
