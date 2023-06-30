from fastapi import APIRouter
from db import db_cart
from models.usermodel.shopping_cart import ShoppingCart
router = APIRouter()
from fastapi import Request
@router.post("/api/cart/get_user_cart/")
def get_user_cart(request: Request):
    token = request.headers.get("token")
    # 在数据库中插入用户信息
    result = db_cart.get_user_cart(token)
    print(result)
    data = {}

    for item in result:
        order_id = 'shoppingcart'
        if order_id not in data:
            data[order_id] = []
        list = {
            "product_id": item[1],
            "quantity": item[2],
            "add_time": item[3]
        }
        data[order_id].append(list)
    # data[item[0]] = data
    return {"code": 200, "message": "shoppingcart get successful", "data": data}