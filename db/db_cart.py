from models.shopping_cart import ShoppingCart
from .database import execute_query


def add_to_cart(shoppingCart: ShoppingCart):
    sql_select = "SELECT quantity FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
    result = execute_query(sql_select, (shoppingCart.user_id, shoppingCart.product_id))
    print(result)
    if result and result[0][0] + shoppingCart.quantity <= 0:
        # 数量减少后小于等于零，删除记录
        sql_delete = "DELETE FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
        execute_query(sql_delete, (shoppingCart.user_id, shoppingCart.product_id))
    elif result:
        # 更新数量
        current_quantity = result[0][0]
        new_quantity = current_quantity + shoppingCart.quantity
        sql_update = "UPDATE Shopping_cart SET quantity = %s WHERE user_id = %s AND product_id = %s"
        execute_query(sql_update, (new_quantity, shoppingCart.user_id, shoppingCart.product_id))
    elif shoppingCart.quantity > 0:
        # 插入新记录
        sql_insert = "INSERT INTO Shopping_cart (user_id, product_id, quantity, add_time) VALUES (%s, %s, %s, %s)"
        execute_query(sql_insert, (shoppingCart.user_id, shoppingCart.product_id, shoppingCart.quantity, shoppingCart.add_time))





def remove_from_cart(shoppingCart: ShoppingCart):
    sql = "DELETE FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
    execute_query(sql, (shoppingCart.user_id, shoppingCart.product_id))

def get_user_cart(shoppingCart: ShoppingCart):
    sql = "SELECT * FROM Shopping_cart WHERE user_id = %s"
    result = execute_query(sql, (shoppingCart.user_id))
    return result