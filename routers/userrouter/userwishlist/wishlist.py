from fastapi import APIRouter
from models.storemodel.product import Product
from db import db_wishlist
from fastapi import Request
router = APIRouter()


@router.post("/api/users/wishlist/")
def wishlist(request: Request):
    token = request.headers.get("Authorization")
    # 把商品加入购物车
    result = db_wishlist.wishlist(token)
    data = []

    for item in result:
        product1 = Product(
            product_id=item[0],
            product_name=item[1],
            product_description=item[2],
            product_price=item[3],
            category_id=item[4],
            product_image=item[5],
            product_status=item[6],
            stock_quantity=item[7]
        )
        data.append(product1)
    data = {"products": data}
    return {"code": 200, "message": "Wishlist got successfully", "data": data}