from fastapi import APIRouter
from db import db_store
from db import db_user
from models.usermodel.user import User
from fastapi import Request
from models.storemodel.product import Product
from utils.auth import decode_token
router = APIRouter()


@router.post("/api/store/productlist/")
def productlist(request: Request):
    token = request.headers.get("Authorization")
    try:
        result1 = db_user.user_info(token)
        for item in result1:
            if item[6] == 'admin':
                result = db_store.productlist1()
            if item[6] == 'customer':
                result = db_store.productlist()
                print(result)
    except:
        result = db_store.productlist()
    # 获取商品列表
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
    return {"code": 200, "message": "Productlist get successful", "data": data}