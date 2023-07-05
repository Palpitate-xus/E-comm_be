from fastapi import APIRouter
from models.usermodel.order_details import OrderDetail
from db import db_orders

router = APIRouter()


@router.post("/api/orders/get_order_details")
def find_history(orderdetail: OrderDetail):
    result = db_orders.get_order_detail1(orderdetail)
    print(result)
    data = {}

    for item in result:

        orderd = 'orderdetails'
        if orderd not in data:
            data[orderd] = []
        list = {
            "order_id": item[1],
            "product_id": item[2],
            "quantity": item[3],
            "product_price": item[4],
            "product_name": item[5]
        }
        data[orderd].append(list)

    return {"code": 200, "message": "Order details got successfully", "data": data}