from models.supplier import Supplier
from .database import execute_query,get_connection,close_connection

def accept_order(supplier:Supplier):
    #将订单数据加入至数据库中
    sql="INSERT INTO "
