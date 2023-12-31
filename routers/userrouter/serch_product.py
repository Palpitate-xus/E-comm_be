from fastapi import APIRouter
from models.storemodel.product import Product
from db import db_store

router = APIRouter()


@router.post("/api/products/search/")
def searchproduct(product: Product):
    # 在数据库中查询商品
    result = db_store.searchproduct(product)
    data = []

    for item in result:
        product1 = Product(
            product_id=item[0],
            product_name=item[1],
            product_description=item[2],
            product_price=item[3],
            category=item[4],
            product_image=item[5],
            product_status=item[6],
            stock_quantity=item[7]
        )
        data.append(product1)
    data = {"products": data}
    return {"code": 200, "message": "Product searched successful", "data": data}

