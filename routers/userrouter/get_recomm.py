from fastapi import APIRouter
from models.storemodel.product import Product
from models.usermodel.orders import Orders
from db import db_orders
from fastapi import Request
router = APIRouter()


@router.post("/api/users/get_recomm")
def get_recomm(request: Request):
    # 获取前端传递的token
    token = request.headers.get("Authorization")
    result = db_orders.get_recomm(token)
    print(result)
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
    return {"code": 200, "message": "Recommandlist get successful", "data": data}