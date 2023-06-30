from fastapi import APIRouter
from db import db_store
from models.storemodel.product import Product
router = APIRouter()


@router.post("/api/store/offshelf/")
def offshelf(product: Product):
    # 在商城中下架商品
    result = db_store.offshelf(product)
    return {"code": 200, "message": "Product offshelf successful", "data": {}}