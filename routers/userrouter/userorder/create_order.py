from fastapi import APIRouter
from models.usermodel.create_order import CreateOrder
from db import db_orders
from fastapi import Request
router = APIRouter()


@router.post("/api/orders/create_order")
def create_order(createorder: CreateOrder, request: Request):
    token = request.headers.get("token")
    #创建订单
    result = db_orders.create_order(createorder, token)
    print(result)
    if result == 1:
        return {"code": 200, "message": "Order create successfully", "data": {}}
    if result == 0:
        return {"code": 403, "message": "Order create failed", "data": {}}