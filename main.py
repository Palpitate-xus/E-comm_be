from fastapi import FastAPI, HTTPException
import jwt
from datetime import datetime, timedelta
import pymysql
app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

# 数据库连接信息
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'Zyf1231234321',
    'database': 'E-commerce_platform',
}

# 创建数据库连接
connection = pymysql.connect(**DB_CONFIG)


@app.on_event("shutdown")
def shutdown_event():
    # 关闭数据库连接
    connection.close()


@app.post("/login")
async def login(username: str, password: str):
    # 创建游标对象
    with connection.cursor() as cursor:
        # 查询数据库中是否存在匹配的用户名和密码
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result is None:
            # 用户名或密码不匹配，返回错误响应
            raise HTTPException(status_code=401, detail="Invalid username or password")
        else:
            # 生成JWT令牌
            payload = {
                "username": username,
                "exp": datetime.utcnow() + timedelta(hours=1)  # 令牌过期时间
            }
            token = jwt.encode(payload, "your_secret_key", algorithm="HS256")

            # 返回包含令牌的成功响应
            return {"token": token}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)