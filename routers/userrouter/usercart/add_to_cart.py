from fastapi import APIRouter
from models.usermodel.shopping_cart import ShoppingCart
from db import db_cart
from fastapi import Request
router = APIRouter()


@router.post("/api/cart/add_to_cart/")
def add_to_cart(shoppingCart: ShoppingCart, request: Request):
    token = request.headers.get("Authorization")
    # 把商品加入购物车
    db_cart.add_to_cart(shoppingCart,token)

    return {"code": 200, "message": "Add to cart successfully", "data": {}}