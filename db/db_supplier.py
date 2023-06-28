from models.supplier import Supplier
from models.product import Product
from models.supply_order import Supply_order
from .database import execute_query,get_connection,close_connection
from datetime import datetime
import uuid

def accept_order(supply_order:Supply_order):
    #将订单数据加入至数据库中
    sql="INSERT INTO Supply_order(supplyorder_id, supplier_id,product_id,quantity,storage_time) VALUES (%s,%s,%s,%s,%s)"
    storage_time=datetime.now()
    supplyorder_id=str(uuid.uuid4())
    result=execute_query(sql,(supplyorder_id,supply_order.supplier_id, supply_order.product_id, supply_order.stock_quantity, storage_time))
