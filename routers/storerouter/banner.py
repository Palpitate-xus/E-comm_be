from fastapi import APIRouter
from db import db_store
from models.usermodel.shopping_cart import ShoppingCart
router = APIRouter()
from fastapi import Request
@router.post("/api/store/banner/")
def get_user_cart():
    result = db_store.banner()
    data = {}

    for item in result:
        chart = 'image'
        if chart not in data:
            data[chart] = []
        list = {
            "id": item[0],
            "image": item[1]
        }
        data[chart].append(list)
    return {"code": 200, "message": "banner get successful", "data": data}