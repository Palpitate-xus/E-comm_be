from models.usermodel.shopping_cart import ShoppingCart
from .database import execute_query
from utils.auth import decode_token

def add_to_cart(shoppingCart: ShoppingCart, token):

    sql_select = "SELECT quantity FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
    result = execute_query(sql_select, (decode_token(token,"your_secret_key")['userid'], shoppingCart.product_id))
    print(result)
    if result and result[0][0] + shoppingCart.quantity <= 0:
        # 数量减少后小于等于零，删除记录
        sql_delete = "DELETE FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
        execute_query(sql_delete, (decode_token(token,"your_secret_key")['userid'], shoppingCart.product_id))
    elif result:
        # 更新数量
        current_quantity = result[0][0]
        new_quantity = current_quantity + shoppingCart.quantity
        sql_update = "UPDATE Shopping_cart SET quantity = %s WHERE user_id = %s AND product_id = %s"
        execute_query(sql_update, (new_quantity, decode_token(token,"your_secret_key")['userid'], shoppingCart.product_id))
    elif shoppingCart.quantity > 0:
        # 插入新记录
        sql_insert = "INSERT INTO Shopping_cart (user_id, product_id, quantity, add_time) VALUES (%s, %s, %s, %s)"
        execute_query(sql_insert, (decode_token(token,"your_secret_key")['userid'], shoppingCart.product_id, shoppingCart.quantity, shoppingCart.add_time))





def remove_from_cart(shoppingCart: ShoppingCart, token):
    sql = "DELETE FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
    execute_query(sql, (decode_token(token,"your_secret_key")['userid'], shoppingCart.product_id))

def get_user_cart(token):
    user_id = decode_token(token, "your_secret_key")['userid']
    sql = """
        SELECT c.*, p.product_price, p.product_name, i.stock_quantity
        FROM Shopping_cart c
        INNER JOIN Product p ON c.product_id = p.product_id
        INNER JOIN Inventory i ON p.product_id = i.product_id
        WHERE c.user_id = %s
    """
    result = execute_query(sql, (user_id,))
    return result
