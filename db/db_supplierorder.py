from models.usermodel.user import User
from models.usermodel.orders import Orders
from models.usermodel.order_details import OrderDetail
from models.suppliermodel.supply_order import Supply_order
from models.suppliermodel.supplier_orderdetails import Supply_orderdetails

import uuid
from models.usermodel.create_order import CreateOrder
from .database import execute_query
from utils.auth import decode_token
from datetime import datetime


def get_order_list(token):
    sql = """SELECT so.* 
          FROM Supply_order so
          INNER JOIN Supplier s ON so.supplier_id = s.supplier_id
          WHERE user_id = %s
          """
    results = execute_query(sql, (decode_token(token,"your_secret_key")['userid']))
    return results

def get_order_detail1(supply_orderdetails:Supply_orderdetails):
    sql = """
        SELECT so.*, p.product_name
        FROM Supply_orderdetail so
        INNER JOIN Product p ON so.product_id = p.product_id
        WHERE so.supplyorder_id = %s
    """
    results = execute_query(sql, (supply_orderdetails.supplyorder_id))
    return results

def accept_order(supply_order: Supply_order):
     sql = "UPDATE supply_order SET order_status = 'shipped' WHERE supplyorder_id = %s"
     execute_query(sql, (supply_order.supplyorder_id))
     sql = "SELECT order_id FROM supply_orderdetail WHERE supplyorder_id = %s"
     result0 = execute_query(sql, (supply_order.supplyorder_id))
     print(result0[0][0])
     sql = """
     SELECT order_status
     FROM Supply_order
     WHERE supplyorder_id IN (SELECT supplyorder_id FROM Supply_orderdetail WHERE order_id = %s)
"""
     result = execute_query(sql, (result0[0][0]))
     print(result)
     for item in result:
         if item[0] != "shipped":
             return 0
     sql = "UPDATE Orders SET order_status = 'has shipped' WHERE order_id = %s"
     execute_query(sql, (result0[0][0]))
     # import smtplib
     # from email.mime.text import MIMEText
     # from email.mime.multipart import MIMEMultipart
     #
     # # 邮件内容
     # message = MIMEMultipart()
     # message["From"] = "3043863274@qq.com"
     # message["To"] = "3043863274@qq.com"
     # message["Subject"] = "邮件主题"
     #
     # # 正文内容
     # body = "这是邮件的正文内容。"
     # message.attach(MIMEText(body, "plain"))
     #
     # # 发送邮件
     # with smtplib.SMTP("smtp.qq.com", 25) as server:
     #     server.starttls()  # 使用TLS加密连接
     #     server.login("3043863274@qq.com", "password")  # 发件人邮箱账号和密码
     #     server.send_message(message)



