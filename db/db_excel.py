import pandas as pd
from db.database import get_connection, close_connection, execute_query
from models.storemodel.product import Product

def add_products_from_excel(file_path):
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
        for product in products:
            sql = """
                INSERT INTO product (product_name, product_description, product_price, category_id, product_image)
                VALUES (%s, %s, %s, %s, %s)
            """
            execute_query(sql, (product.product_name, product.product_description, product.product_price, product.category_id,
                                      product.product_image))
        return True

    except Exception as e:
        print(f"Error adding products from Excel: {e}")
        return False
