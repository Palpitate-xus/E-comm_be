import jwt
from datetime import datetime, timedelta

# 生成token
def generate_token(userid):
    secret_key = "your_secret_key"  # 密钥
    payload = {
        "userid": userid,
        "exp": datetime.utcnow() + timedelta(hours=24)  # 令牌过期时间
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


def decode_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # 令牌已过期
        return "Token has expired."
    except jwt.InvalidTokenError:
        # 无效的令牌
        return "Invalid token."