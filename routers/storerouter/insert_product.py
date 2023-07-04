from fastapi import APIRouter
from db import db_product
from models.storemodel.product import Product
router=APIRouter()

@router.post("/api/store/insert_product")
def insert_product(product:Product):
    db_product.insert_product(product)
    return {"code": 200, "message": "Product insert successful", "data": {}}

