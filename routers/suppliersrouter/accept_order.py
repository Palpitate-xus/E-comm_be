from fastapi import APIRouter
from models.supplier import Supplier
from db import db_user


router = APIRouter()
@router.post("/api/suppliers/accept_order")
def accept_order(supplier: Supplier):
    # 处理供应商接受订单的逻辑
    # 根据supplier对象的属性执行相应的操作
    return {"message": "Order accepted by supplier"}