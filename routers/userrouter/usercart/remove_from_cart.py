from fastapi import APIRouter
from models.usermodel.shopping_cart import ShoppingCart
from db import db_cart
from fastapi import Request
router = APIRouter()


@router.post("/api/cart/remove_from_cart")
def remove_from_cart(shoppingCart: ShoppingCart, request: Request):
    # 获取前端传递的token
    token = request.headers.get("token")
    # 在数据库中插入商品信息
    db_cart.remove_from_cart(shoppingCart,token)
    return {"code": 200, "message": "Remove from cart successfully", "data": {}}