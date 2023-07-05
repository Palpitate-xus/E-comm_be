from fastapi import APIRouter
from db import db_product
from models.storemodel.product import Product
router=APIRouter()
from fastapi import Request
@router.post("/api/store/insert_product")
def insert_product(request: Request, product:Product):
    token = request.headers.get("Authorization")
    db_product.insert_product(product, token)
    return {"code": 200, "message": "Product insert successful", "data": {}}

