from fastapi import APIRouter
from models.order_details import OrderDetail
from models.order_details import OrderDetail
from db import db_orders

router = APIRouter()


@router.post("/api/orders/get_order_details")
def find_history(orderdetail: OrderDetail):
    result = db_orders.get_order_detail(orderdetail)
    print(result)
    data = []

    for item in result:
        product = OrderDetail(
            order_id = item[0],
            product_id = item[1],
            quantity = item[2],
            unit_price = item[3]
        )
        data.append(product)
    data = {"orderdetails": data}
    return {"code": 200, "message": "Order details got successfully", "data": data}