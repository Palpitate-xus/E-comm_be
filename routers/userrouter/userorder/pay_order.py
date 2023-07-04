from fastapi import APIRouter
from db import db_orders
from fastapi import Request
from utils import qr_code
router = APIRouter()

@router.get("/api/payments/qrcode_pay/{order_id}")
def pay_order(order_id):
    print(order_id)
    db_orders.pay_order(order_id)
    return "支付成功"