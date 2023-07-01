from models.usermodel.user import User
from models.usermodel.address import Address
from datetime import datetime
from models.usermodel.wishlist import Wishlist
from db.database import execute_query,get_connection,close_connection
from utils.auth import decode_token


def add_to_wishlist(wishlist: Wishlist, token):
    sql = "SELECT * FROM Wishlist WHERE product_id = %s AND user_id = %s"
    result = execute_query(sql, (wishlist.product_id, decode_token(token, "your_secret_key")['userid']))
    if len(result) == 1:
        return 0
    else:
        sql = "INSERT INTO Wishlist (product_id, user_id, add_time) VALUES (%s, %s, %s)"
        execute_query(sql, (wishlist.product_id, decode_token(token, "your_secret_key")['userid'], datetime.now()))

def remove_from_wishlist(wishlist: Wishlist, token):
    sql = "DELETE FROM Wishlist WHERE product_id = %s AND user_id = %s"
    execute_query(sql, (wishlist.product_id, decode_token(token, "your_secret_key")['userid']))

def wishlist(token):
    sql = """SELECT p.*, i.stock_quantity
FROM Product p
INNER JOIN Inventory i ON p.product_id = i.product_id
INNER JOIN Wishlist w ON p.product_id = w.product_id
WHERE w.user_id = %s
    AND p.product_status = 'active'"""
    result = execute_query(sql, (decode_token(token, "your_secret_key")['userid']))
    return result