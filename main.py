from fastapi import FastAPI
from routers import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 设置 CORS 配置
origins = [
    "http://localhost",
    "http://localhost:5137",
    "*",
    # 添加其他允许访问的域名/地址
]

# 启用 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#用户信息管理路由
app.include_router(login_router)
app.include_router(logout_router)
app.include_router(signup_router)
app.include_router(reset_password_router)
app.include_router(update_profile_router)
app.include_router(get_profile_router)
app.include_router(rsa_router)
app.include_router(userinfo_router)
#用户地址管理
app.include_router(create_address_router)
app.include_router(addresslist_router)
app.include_router(delete_address_router)
#用户搜索商品路由
app.include_router(serch_product_router)
#用户愿望单路由
app.include_router(add_to_wishlist_router)
app.include_router(remove_from_wishlist_router)
app.include_router(wishlist_router)
#用户购物车管理路由
app.include_router(add_to_cart_router)
app.include_router(remove_from_cart_router)
app.include_router(get_user_cart_router)
#用户订单管理
app.include_router(create_order_router)
app.include_router(remove_order_router)
app.include_router(pay_order_router)
app.include_router(qrcodepay_router)
app.include_router(get_order_details_router)
app.include_router(get_order_list_router)
#商城订单和商品管理
app.include_router(productlist_router)
app.include_router(offshelf_router)
app.include_router(onshelf_router)
app.include_router(orderlist_router)
app.include_router(accept_order_platform_router)
app.include_router(reject_order_platform_router)
#供应商接受订单
app.include_router(accept_order_supplier_router)
app.include_router(get_supplierorder_router)
#供应商库存管理
app.include_router(inventory_management_router)
app.include_router(upload_products_from_excel)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)