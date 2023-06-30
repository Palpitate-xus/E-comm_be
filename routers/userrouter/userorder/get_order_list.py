from fastapi import APIRouter
from models.usermodel.user import User
from models.usermodel.orders import Orders
from db import db_orders
from fastapi import Request
router = APIRouter()


@router.post("/api/orders/get_order_list")
def get_order_list(request: Request):
    # 获取前端传递的token
    token = request.headers.get("Authorization")
    result = db_orders.get_order_list(token)
    print(result)
    data = []

    for item in result:
        orders = Orders(
            order_id=item[0],
            user_id=item[1],
            order_status=item[2],
            total_amount=item[3],
            order_time=item[4],
            payment_status=item[5],
            payment_method=item[6],
            shipping_address=item[7]
        )

        data.append(orders)
    data = {"orders": data}
    return {"code": 200, "message": "orders got successfully", "data": data}