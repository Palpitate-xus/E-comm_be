from fastapi import APIRouter
from models.suppliermodel.inventory import Inventory
from db.database import get_connection, close_connection
from db import db_inventory

router = APIRouter()
@router.post("/api/suppliers/inventory_management")
def inventory_management(inventory: Inventory):
    connection = get_connection()
    # 在这里使用连接对象执行插入库存数据的操作，可以根据实际需求编写逻辑
    db_inventory.inventory_management(inventory)
    # 插入完成后，记得关闭连接
    close_connection(connection)

    return {"code": 200, "message": "Inventory changed successfully"}