from fastapi import APIRouter
from models.shopping_cart import ShoppingCart
from db import db_cart

router = APIRouter()


@router.post("/api/cart/remove_from_cart")
def remove_from_cart(shoppingCart: ShoppingCart):
    # 在数据库中插入商品信息
    db_cart.remove_from_cart(shoppingCart)

    return {"code": 200, "message": "Remove from cart successfully", "data": {}}