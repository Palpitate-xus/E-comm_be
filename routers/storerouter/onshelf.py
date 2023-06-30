from fastapi import APIRouter
from db import db_store
from models.storemodel.product import Product
router = APIRouter()


@router.post("/api/store/onshelf/")
def onshelf(product: Product):
    # 在商城中上架商品
    result = db_store.onshelf(product)
    return {"code": 200, "message": "Product onshelf successful", "data": {}}