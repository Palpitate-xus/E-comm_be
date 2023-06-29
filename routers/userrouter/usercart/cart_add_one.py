from fastapi import APIRouter
from models.shopping_cart import ShoppingCart
from db import db_cart

router = APIRouter()


@router.post("/api/cart/cart_add_one/")
def add_to_cart(shoppingCart: ShoppingCart):
    # 在数据库中插入商品信息
    db_cart.cart_add_one(shoppingCart)

    return {"code": 200, "message": "Add to cart successfully", "data": {}}