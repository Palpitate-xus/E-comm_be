from models.shopping_cart import ShoppingCart
from .database import execute_query


def add_to_cart(shoppingCart: ShoppingCart):
    sql = "INSERT INTO Shopping_cart (user_id, product_id, quantity, add_time) VALUES (%s, %s, %s, %s)"
    execute_query(sql, (shoppingCart.user_id, shoppingCart.product_id, shoppingCart.quantity, shoppingCart.add_time))

def remove_from_cart(shoppingCart: ShoppingCart):
    sql = "DELETE FROM Shopping_cart WHERE user_id = %s AND product_id = %s"
    execute_query(sql, (shoppingCart.user_id, shoppingCart.product_id))

def get_user_cart(shoppingCart: ShoppingCart):
    sql = "SELECT * FROM Shopping_cart WHERE user_id = %s"
    result = execute_query(sql, (shoppingCart.user_id))
    return result