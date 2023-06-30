from fastapi import APIRouter
from db import db_store
from models.storemodel.product import Product
router = APIRouter()


@router.post("/api/store/productlist/")
def productlist():
    # 在数据库中插入用户信息
    result = db_store.productlist()
    data = []

    for item in result:
        product1 = Product(
            product_id=item[0],
            product_name=item[1],
            product_description=item[2],
            product_price=item[3],
            category_id=item[4],
            product_image=item[5],
            stock_quantity=item[6]
        )
        data.append(product1)
    data = {"products": data}
    return {"code": 200, "message": "Productlist get successful", "data": data}