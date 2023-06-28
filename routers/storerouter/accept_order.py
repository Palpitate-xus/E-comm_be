from fastapi import APIRouter
from models.user import User
from models.orders import Orders
from db import db_store

router = APIRouter()


@router.post("/api/store/accept_order/")
def accept_order(orders: Orders):
    db_store.accept_order(orders)

    return {"code": 200, "message": "Order accepted", "data": {}}
