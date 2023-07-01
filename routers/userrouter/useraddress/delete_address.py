from fastapi import APIRouter
from models.usermodel.address import Address
from db import db_address
from fastapi import Request
router = APIRouter()


@router.post("/api/users/delete_address/")
def delete_address(adress: Address, request: Request):
    token = request.headers.get("Authorization")
    # 删除地址
    db_address.delete_address(adress, token)

    return {"code": 200, "message": "Address deleted successfully", "data": {}}