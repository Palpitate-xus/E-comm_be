from fastapi import APIRouter
from db import db_store
from models.storemodel.product import Product
router = APIRouter()


@router.post("/api/store/delete_product")
def delete_product():
    # 在数据库中插入用户信息
    result = db_store.delete_product()
    return {"code": 200, "message": "Product deleted successful", "data": {}}