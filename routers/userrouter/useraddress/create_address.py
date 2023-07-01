from fastapi import APIRouter
from models.usermodel.address import Address
from db import db_address
from fastapi import Request
router = APIRouter()


@router.post("/api/users/create_address/")
def create_address(adress: Address, request: Request):
    token = request.headers.get("Authorization")
    # 创建地址
    db_address.create_address(adress, token)

    return {"code": 200, "message": "Address created successfully", "data": {}}