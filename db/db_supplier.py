from models.suppliermodel.supply_order import Supply_order
from .database import execute_query
def accept_order(supply_order: Supply_order):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # 检查订单是否存在
            sql = "SELECT * FROM supply_order WHERE supplyorder_id = %s"
            cursor.execute(sql, supply_order.supplyorder_id)
            result = cursor.fetchone()

            if result is None:
                # 如果订单不存在，则将其插入表中并将 order_status 列设为 'accept'
                sql = "INSERT INTO supply_order (supplyorder_id, supplier_id, order_status, order_time) " \
                      "VALUES (%s, %s, 'pending', %s)"
                cursor.execute(sql, (supply_order.supplyorder_id, supply_order.supplier_id, supply_order.order_time))
                connection.commit()
            else:
                # 如果订单存在，则将其 order_status 列修改为 'accept'
                sql = "UPDATE supply_order SET order_status = 'accept' WHERE supplyorder_id = %s"
                cursor.execute(sql, supply_order.supplyorder_id)
                connection.commit()

        return {"message": "订单已接收"}

    finally:
        close_connection(connection)
