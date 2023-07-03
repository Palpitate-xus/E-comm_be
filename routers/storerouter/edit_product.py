from fastapi import APIRouter
from db import db_product
from models.storemodel.product import Product
from db.database import get_connection, close_connection
router=APIRouter()

@router.post("/api/store/edit_product")
def edit_product(product:Product):
    #在商品表中修改数据
    connection = get_connection()
    result=db_product.edit_product(product)
    close_connection(connection)
    return {"code": 200, "message": "Product edit successful", "data": {}}