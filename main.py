from fastapi import FastAPI
from routers import *

app = FastAPI()
app.include_router(login_router)
app.include_router(signup_router)
app.include_router(reset_password_router)
app.include_router(update_profile_router)
app.include_router(productlist_router)
app.include_router(accept_order_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)