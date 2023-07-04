from fastapi import APIRouter
from models.suppliermodel.supply_order import Supply_order
from db import db_supplierorder


router = APIRouter()
@router.post("/api/supplier/accept_order")
def accept_order(supply_order: Supply_order):
    # 处理供应商接受订单的逻辑
    db_supplierorder.accept_order(supply_order)
    #print(result[0])

    # 根据supplier对象的属性执行相应的操作
    return {"code": 200, "message": "Order accepted by supplier", "data": {}}