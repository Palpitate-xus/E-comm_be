from fastapi import APIRouter
from db import db_user
from models.usermodel.user import User
from fastapi import Request
router = APIRouter()

@router.post("/api/users/get_profile/")
def get_profile(request: Request):
    # 获取前端传递的token
    token = request.headers.get("Authorization")
    # 更新密码
    result = db_user.get_profile(token)
    data = []
    print(result)
    for item in result:
        orders = User(
            user_id = item[0],
            username = item[1],
            password = item[2],
            email = item[3],
            registration_date = item[4],
            last_login_date = item[5],
            user_type=item[6],
            user_status = item[7]
        )

        data.append(orders)
    # data = {"userprofile": data[0]}
    return {"code": 200, "message":   "Profile got successfully", "data": data[0]}