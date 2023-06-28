from models.supplier import Supplier
from models.product import Product
from .database import execute_query,get_connection,close_connection
from datetime import datetime

def accept_order(supplier:Supplier):
    #将订单数据加入至数据库中
    sql="INSERT INTO Supply_order(supplier_id,product_id,quantity,storage_time) VALUES (%s %s %s %s)"
    storage_time=datetime.now()
    result=execute_query(sql,(Supplier.supplier_id, Product.product_id, Product.stock_quantity, storage_time))
