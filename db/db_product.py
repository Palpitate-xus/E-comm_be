#对商品表插入数据、删除数据和修改数据
from models.storemodel.product import Product
from .database import execute_query,get_connection,close_connection

def delete_product(product:Product):
    connection = get_connection()
    try:
        sql = "DELETE FROM product WHERE product_id = %s"
        execute_query(sql,product.product_id)
    finally:
        close_connection(connection)

def edit_product(product:Product):
    connection = get_connection()
    try:
        sql = """
                        UPDATE product
                        SET product_name = %s,
                            product_description = %s,
                            product_price = %s,
                            category_id = %s,
                            product_image = %s,
                            product_status = %s
                        WHERE product_id = %s
                    """
        execute_query(sql,(product.product_name,product.product_description,
                           product.product_price,product.category_id,
                           product.product_image,product.product_status,product.product_id))
    finally:
        close_connection(connection)

def insert_product(product:Product):
    connection = get_connection()
    try:
        sql = """
                        INSERT INTO product
                        (product_id, product_name, product_description, product_price, category_id, product_image, product_status)
                        VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                    """
        execute_query(sql,(product.product_id,product.product_name,product.product_description,
                           product.product_price,product.category_id,product.product_image,
                           product.product_status))

    finally:
        close_connection(connection)