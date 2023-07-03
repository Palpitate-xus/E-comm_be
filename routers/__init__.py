#用户个人信息
from routers.userrouter.userinformation.reset_password import router as reset_password_router
from routers.userrouter.userinformation.login import router as login_router
from routers.userrouter.userinformation.logout import router as logout_router
from routers.userrouter.userinformation.signup import router as signup_router
from routers.userrouter.userinformation.update_profile import router as update_profile_router
from routers.userrouter.userinformation.get_profile import router as get_profile_router
from routers.userrouter.userinformation.userinfo import router as userinfo_router
#用户其他功能
from .userrouter.serch_product import router as serch_product_router
#用户愿望单
from routers.userrouter.userwishlist.add_to_wishlist import router as add_to_wishlist_router
from routers.userrouter.userwishlist.remove_from_wishlist import router as remove_from_wishlist_router
from routers.userrouter.userwishlist.wishlist import router as wishlist_router
#用户地址
from routers.userrouter.useraddress.create_address import router as create_address_router
from routers.userrouter.useraddress.addresslist import router as addresslist_router
from routers.userrouter.useraddress.delete_address import router as delete_address_router
#用户购物车
from routers.userrouter.usercart.remove_from_cart import router as remove_from_cart_router
from routers.userrouter.usercart.add_to_cart import router as add_to_cart_router
from routers.userrouter.usercart.get_user_cart import router as get_user_cart_router
#用户订单
from routers.userrouter.userorder.create_order import router as create_order_router
from routers.userrouter.userorder.get_order_details import router as get_order_details_router
from routers.userrouter.userorder.get_order_list import router as get_order_list_router
from routers.userrouter.userorder.pay_order import router as pay_order_router
from routers.userrouter.userorder.qrcodepay import router as qrcodepay_router
from routers.userrouter.userorder.remove_order import router as remove_order_router
#商店
from .storerouter.productlist import router as productlist_router
from .storerouter.offshelf import router as offshelf_router
from .storerouter.onshelf import router as onshelf_router
from .storerouter.orderlist import router as orderlist_router
from .storerouter.accept_order import router as accept_order_platform_router
from .storerouter.reject_order import router as reject_order_platform_router
#供应商
from .suppliersrouter.accept_order import router as accept_order_supplier_router
from .suppliersrouter.inventory_management import router as inventory_management_router
from .suppliersrouter.commodity_update import router as upload_products_from_excel
from .suppliersrouter.orderlist import router as get_supplierorder_router
from routers.userrouter.rsa import router as rsa_router


