from fastapi import APIRouter
from models.usermodel.user import User
from models.suppliermodel.supply_order import Supply_order
from db import db_supplierorder
from fastapi import Request
router = APIRouter()


@router.post("/api/supplier/get_order_list")
def get_order_list(request: Request):
    # 获取前端传递的token
    token = request.headers.get("Authorization")
    print(token)
    result = db_supplierorder.get_order_list(token)
    data = []

    for item in result:
        so = Supply_order(
        supplyorder_id= item[0],
        supplier_id= item[1],
        order_status= item[2],
        order_time= item[3]
        )

        data.append(so)
    data = {"supplier_orders": data}
    return {"code": 200, "message": "orders got successfully", "data": data}