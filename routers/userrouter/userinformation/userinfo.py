from fastapi import APIRouter
from models.usermodel.userinfo import Userinfo
from db import db_user
router = APIRouter()


@router.post("/api/users/userInfo/")
def userinfo(userinfo: Userinfo):
    token = userinfo.Authorization
    result = db_user.user_info(token)
    data = {}
    for item in result:
        a = "permissions"
        data[a] = []
        data[a].append(item[6])
        b = "username"
        data[b] = item[1]
        c = "avatar"
        data[c] = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202006%2F07%2F20200607000651_vopye.jpg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1672814873&t=b4388830c9cf3005e51d64f282b07abc"
    print(data)
    return {"code": 200, "msg": 'success', "data": data}