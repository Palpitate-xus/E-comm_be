from fastapi import APIRouter
from db import db_product
from models.storemodel.product import Product
from db.database import get_connection, close_connection
router=APIRouter()

@router.post("/api/store/insert_product")
def insert_product(product:Product):
    #在商品表中增加一条数据
    connection = get_connection()
    result=db_product.insert_product(product)
    close_connection(connection)
    return {"code": 200, "message": "Product insert successful", "data": {}}

