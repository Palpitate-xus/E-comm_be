from fastapi import APIRouter
from models.usermodel.orders import Orders
from db import db_orders

router = APIRouter()


@router.post("/api/users/retuen_order")
def retuen_order(orders: Orders):
    # 在数据库中插入商品信息
    db_orders.retuen_order(orders)

    return {"code": 200, "message": "Order remove successfully", "data": {}}