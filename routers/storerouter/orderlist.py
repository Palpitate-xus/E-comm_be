from fastapi import APIRouter
from models.user import User
from models.orders import Orders
from db import db_store

router = APIRouter()


@router.post("/api/store/orderlist/")
def get_order_list():
    result = db_store.orderlist()
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
    data = {"orderlist": data}
    return {"code": 200, "message": "Orderlist got successfully", "data": data}