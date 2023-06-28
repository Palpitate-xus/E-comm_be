from fastapi import APIRouter
from models.create_order import CreateOrder
from db import db_orders

router = APIRouter()


@router.post("/api/orders/create_order")
def create_order(createorder: CreateOrder):
    # 在数据库中插入商品信息
    db_orders.create_order(createorder)

    return {"code": 200, "message": "Order create successfully", "data": {}}