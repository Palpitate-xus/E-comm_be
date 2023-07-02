from fastapi import APIRouter
from models.usermodel.wishlist import Wishlist
from db import db_wishlist
from fastapi import Request
router = APIRouter()


@router.post("/api/users/remove_from_wishlist/")
def remove_from_wishlist(wishlist: Wishlist, request: Request):
    token = request.headers.get("Authorization")
    # 把商品加入购物车
    db_wishlist.remove_from_wishlist(wishlist,token)
    return {"code": 200, "message": "Remove from wishlist successfully", "data": {}}