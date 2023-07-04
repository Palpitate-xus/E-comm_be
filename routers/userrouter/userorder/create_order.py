from fastapi import APIRouter
from models.usermodel.create_order import CreateOrder
from db import db_orders
from fastapi import Request
from utils import qr_code
router = APIRouter()


@router.post("/api/orders/create_order/")
def create_order(createorder: CreateOrder, request: Request):
    token = request.headers.get("Authorization")
    #创建订单
    result = db_orders.create_order(createorder, token)
    print(result)
    if result == 0:
        return {"code": 403, "message": "Order create failed", "data": {}}
    else:
        qr_coderesult = qr_code.generate_qr_code("http://mall.iyigui.cn:8000/api/payments/qrcode_pay/"  + result[0][0])
        return {"code": 200, "message": "Order create successfully", "data": {"qr_code": qr_coderesult}}