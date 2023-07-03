import pandas as pd
from db.database import get_connection, close_connection, execute_query
from models.storemodel.product import Product
from datetime import datetime
from utils.auth import decode_token
def add_products_from_excel(file_path, token):
    try:
        print(file_path)
        # 读取Excel文件
        df = pd.read_excel(file_path)
        print(df)
        # 将数据转换为Product对象列表
        products = []
        for _, row in df.iterrows():
            product = Product(
                product_name=row['商品名称'],
                product_description=row['商品描述'],
                product_price=row['商品价格'],
                category_id=row['商品分类'],
                stock_quantity=row['商品库存数量'],
                product_image=row['商品图片']
            )
            products.append(product)
        print(products)
        # 将数据插入到数据库中
        sql = "SELECT supplier_id FROM Supplier WHERE user_id = %s"
        result = execute_query(sql, (decode_token(token, "your_secret_key")['userid']))
        connection = get_connection()
        cur = connection.cursor()
        for product in products:
            sql = """
                INSERT INTO product (product_name, product_description, product_price, category_id, product_image, product_status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql,(product.product_name, product.product_description, product.product_price, product.category_id, product.product_image, 'active'))
            lid = cur.lastrowid
            sql_insert = "INSERT INTO inventory (supplier_id, product_id, inventory_time, stock_quantity) VALUES (%s, %s, %s, %s)"
            execute_query(sql_insert,
                          (result[0][0], lid, datetime.now(), product.stock_quantity))
        return True
        connection = close_connection()
    except Exception as e:
        print(f"Error adding products from Excel: {e}")
        return False
