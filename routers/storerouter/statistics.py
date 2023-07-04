from fastapi import APIRouter
from db import db_orders
from models.usermodel.shopping_cart import ShoppingCart
router = APIRouter()
from fastapi import Request
@router.post("/api/store/statistics/")
def get_user_cart():
    result = db_orders.statistics()
    data = {}

    for item in result:
        chart = 'statistics'
        if chart not in data:
            data[chart] = []
        list = {
            "date": item[0],
            "ordercount": item[1],
            "total_amount": item[2]
        }
        data[chart].append(list)
    return {"code": 200, "message": "Statistic get successful", "data": data}