from fastapi import APIRouter
from models.supply_order import Supply_order
from db import db_supplier


router = APIRouter()
@router.post("/api/suppliers/accept_order")
def accept_order(supply_order: Supply_order):
    # 处理供应商接受订单的逻辑
    result=db_supplier.accept_order(supply_order)
    #print(result[0])

    # 根据supplier对象的属性执行相应的操作
    return {"message": "Order accepted by supplier"}