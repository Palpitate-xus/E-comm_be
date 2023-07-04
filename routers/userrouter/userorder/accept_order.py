from fastapi import APIRouter
from models.usermodel.orders import Orders
from db import db_orders

router = APIRouter()


@router.post("/api/users/accept_order/")
def accept_order(orders: Orders):
    db_orders.accept_order(orders)

    return {"code": 200, "message": "Order accepted", "data": {}}
