from fastapi import APIRouter
from models.usermodel.wishlist import Wishlist
from db import db_wishlist
from fastapi import Request
router = APIRouter()


@router.post("/api/users/add_to_wishlist/")
def add_to_wishlist(wishlist: Wishlist, request: Request):
    token = request.headers.get("Authorization")
    # 把商品加入购物车
    result = db_wishlist.add_to_wishlist(wishlist,token)
    if result == 0:
        return {"code": 403, "message": "Product already in wishlist", "data": {}}
    return {"code": 200, "message": "Add to wishlist successfully", "data": {}}