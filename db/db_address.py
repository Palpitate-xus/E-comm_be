from models.usermodel.user import User
from models.usermodel.address import Address
from datetime import datetime
from models.usermodel.wishlist import Wishlist
from db.database import execute_query,get_connection,close_connection
from utils.auth import decode_token


def create_address(address: Address, token):
    sql = "INSERT INTO Address (user_id, recipient_name, phone_number, province, city, street, postal_code, is_default) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    execute_query(sql, (decode_token(token, "your_secret_key")['userid'], address.recipient_name, address.phone_number, address.province, address.city, address.street, address.postal_code, address.is_default))

def delete_address(address: Address, token):
    sql = "DELETE FROM Address WHERE address_id = %s AND user_id = %s"
    params = (address.address_id, decode_token(token, "your_secret_key")['userid'])
    execute_query(sql, params)

def addresslist(token):
    sql = "SELECT * FROM Address WHERE user_id = %s"
    result = execute_query(sql, (decode_token(token, "your_secret_key")['userid']))
    return result
