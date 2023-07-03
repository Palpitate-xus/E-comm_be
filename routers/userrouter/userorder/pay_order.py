from fastapi import APIRouter
from db import db_orders
from fastapi import Request
from utils import qr_code
router = APIRouter()

@router.get("/api/payments/qrcode_pay/")
def pay_order(order_id: str = None):
    db_orders.pay_order(order_id)
    return 1