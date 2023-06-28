from fastapi import APIRouter
from models.orders import Orders
from db import db_orders

router = APIRouter()


@router.post("/api/orders/create_order")
def create_order(orders: Orders):
    # 在数据库中插入商品信息
    db_orders.create_order(orders)

    return {"code": 200, "message": "Order create successfully", "data": {}}