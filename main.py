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

app.include_router(login_router)
app.include_router(signup_router)
app.include_router(reset_password_router)
app.include_router(update_profile_router)


app.include_router(productlist_router)
app.include_router(accept_order_router)
app.include_router(serch_product_router)
app.include_router(add_to_cart_router)
app.include_router(remove_from_cart_router)
app.include_router(create_order_router)
app.include_router(remove_ordert_router)
app.include_router(pay_order_router)
app.include_router(get_order_details)
app.include_router(get_order_list_router)
app.include_router(get_user_cart_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)