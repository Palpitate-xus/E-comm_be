from models.suppliermodel.inventory import Inventory
from .database import execute_query


def inventory_management(inventory: Inventory):
    sql_select = "SELECT stock_quantity FROM inventory WHERE supplier_id = %s AND product_id = %s"
    result = execute_query(sql_select, (inventory.supplier_id, inventory.product_id))
    print(result)
    if result and result[0][0] + inventory.stock_quantity <= 0:
        # 数量减少后小于等于零，删除记录
        sql_delete = "DELETE FROM inventory WHERE supplier_id = %s AND product_id = %s"
        execute_query(sql_delete, (inventory.supplier_id, inventory.product_id))
    elif result:
        # 更新数量
        current_num = result[0][0]
        new_num = current_num + inventory.stock_quantity
        sql_update = "UPDATE inventory SET stock_quantity = %s WHERE supplier_id = %s AND product_id = %s"
        execute_query(sql_update, (new_num, inventory.supplier_id, inventory.product_id))
    elif inventory.stock_quantity > 0:
        # 插入新记录
        sql_insert = "INSERT INTO inventory (supplier_id, product_id, inventory_time, stock_quantity) VALUES (%s, %s, %s, %s)"
        execute_query(sql_insert, (inventory.supplier_id,inventory.product_id,inventory.inventory_time,inventory.stock_quantity))
