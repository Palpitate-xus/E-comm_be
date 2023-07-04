from fastapi import APIRouter
from models.suppliermodel.supplier_orderdetails import Supply_orderdetails
from db import db_supplierorder

router = APIRouter()


@router.post("/api/suppplier/get_order_details")
def find_history(supply_orderdetails: Supply_orderdetails):
    result = db_supplierorder.get_order_detail1(supply_orderdetails)
    print(result)
    data = {}

    for item in result:

        orderd = 'orderdetails'
        if orderd not in data:
            data[orderd] = []
        list = {
            "order_id": item[0],
            "product_id": item[1],
            "quantity": item[2],
            "product_price": item[3],
            "product_name": item[4]
        }
        data[orderd].append(list)

    return {"code": 200, "message": "Order details got successfully", "data": data}