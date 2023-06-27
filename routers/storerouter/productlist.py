from fastapi import APIRouter
from db import db_store
from models.product import Product
router = APIRouter()


@router.post("/api/store/productlist/")
def reset_password():
    # 在数据库中插入用户信息
    result = db_store.productlist()
    print(result)
    data = []

    for item in result:
        product = Product(
            product_id=item[0],
            product_description=item[1],
            product_price=item[2],
            category_id=item[3],
            stock_quantity=item[4],
            product_image=item[5]
        )
        data.append(product)
    data = {"products": data}
    return {"code": 200, "message": "Productlist get successful", "data": data}