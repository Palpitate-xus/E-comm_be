from fastapi import APIRouter
from models.user import User
from models.orders import Orders
from db import db_store

router = APIRouter()


@router.post("/api/store/reject_order/")
def reject_order(orders: Orders):
    db_store.reject_order(orders)

    return {"code": 200, "message": "Order rejected", "data": {}}