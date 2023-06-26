import jwt
from datetime import datetime, timedelta

#生成token
def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=24)  # 令牌过期时间
    }
    token = jwt.encode(payload, "your_secret_key", algorithm="HS256")
    return token
