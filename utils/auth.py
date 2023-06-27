import jwt
from datetime import datetime, timedelta

# 生成token
def generate_token(userid):
    secret_key = "your_secret_key"  # 密钥
    payload = {
        "username": userid,
        "exp": datetime.utcnow() + timedelta(hours=24)  # 令牌过期时间
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token
