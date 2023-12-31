from fastapi import APIRouter
from models.usermodel.orders import Orders
from db import db_orders
from fastapi import Request
from utils import qr_code
router = APIRouter()


@router.post("/api/payments/pay_order")
def pay_order(orders: Orders, request: Request):
    token = request.headers.get("Authorization")
    # db_orders.pay_order(orders, token)
    # order_details = db_orders.get_order_detail(orders.order_id)
    qr_coderesult = qr_code.generate_qr_code("http://localhost:8000/api/payments/qrcode_pay/" + orders.order_id)
    return {"code": 200, "message": "Order paid successfully", "data": {"qr_code": qr_coderesult}}