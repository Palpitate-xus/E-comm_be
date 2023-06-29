from routers.userrouter.userinformation.reset_password import router as reset_password_router
from routers.userrouter.userinformation.login import router as login_router
from routers.userrouter.userinformation.signup import router as signup_router
from routers.userrouter.userinformation.update_profile import router as update_profile_router

from .userrouter.serch_product import router as serch_product_router

from routers.userrouter.usercart.remove_from_cart import router as remove_from_cart_router
from routers.userrouter.usercart.add_to_cart import router as add_to_cart_router
from routers.userrouter.usercart.get_user_cart import router as get_user_cart_router

from routers.userrouter.userorder.create_order import router as create_order_router
from routers.userrouter.userorder.get_order_details import router as get_order_details_router
from routers.userrouter.userorder.get_order_list import router as get_order_list_router
from routers.userrouter.userorder.pay_order import router as pay_order_router
from routers.userrouter.userorder.remove_order import router as remove_order_router

from .storerouter.productlist import router as productlist_router
from .storerouter.orderlist import router as orderlist_router
from .storerouter.accept_order import router as accept_order_platform_router
from .storerouter.reject_order import router as reject_order_platform_router

from .suppliersrouter.accept_order import router as accept_order_router