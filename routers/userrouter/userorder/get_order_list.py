from fastapi import APIRouter
from models.user import User
from models.orders import Orders
from db import db_orders

router = APIRouter()


@router.post("/api/orders/get_order_list")
def get_order_list(user: User):
    result = db_orders.get_order_list(user)
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