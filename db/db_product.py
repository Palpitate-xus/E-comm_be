#对商品表插入数据、删除数据和修改数据
from models.storemodel.product import Product
from db.database import get_connection, close_connection, execute_query
from utils.auth import decode_token
from datetime import datetime
def delete_product(product:Product):
    connection = get_connection()
    try:
        sql = "DELETE FROM product WHERE product_id = %s"
        execute_query(sql,product.product_id)
    finally:
        close_connection(connection)

def edit_product(product:Product):
    sql = """
            UPDATE product
            SET product_name = %s,
                product_description = %s,
                product_price = %s,
                category = %s,
                product_image = %s,
                product_status = %s
            WHERE product_id = %s
                    """
    execute_query(sql,(product.product_name,product.product_description,
                           product.product_price,product.category,
                           product.product_image,product.product_status,product.product_id))

def insert_product(product:Product, token):
    sql = "SELECT supplier_id FROM Supplier WHERE user_id = %s"
    result = execute_query(sql, (decode_token(token, "your_secret_key")['userid']))
    connection = get_connection()
    cur = connection.cursor()
    sql = """
            INSERT INTO product
            (product_id, product_name, product_description, product_price, category, product_image, product_status)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        """
    cur.execute(sql,(product.product_id,product.product_name,product.product_description,
                           product.product_price,product.category,product.product_image,
                           'active'))
    lid = cur.lastrowid
    sql_insert = "INSERT INTO inventory (supplier_id, product_id, inventory_time, stock_quantity) VALUES (%s, %s, %s, %s)"
    execute_query(sql_insert,(result[0][0], lid, datetime.now(), product.stock_quantity))