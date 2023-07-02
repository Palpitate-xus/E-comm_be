from fastapi import APIRouter
from db import db_address
from fastapi import Request
router = APIRouter()


@router.post("/api/users/addresslist/")
def create_address(request: Request):
    token = request.headers.get("Authorization")
    # 地址列表
    result = db_address.addresslist(token)
    data = {}

    for item in result:
        ad = 'address'
        if ad not in data:
            data[ad] = []
        address = {
            "address_id": item[0],
            "user_id": item[1],
            "recipient_name": item[2],
            "phone_number": item[3],
            "province": item[4],
            "city": item[5],
            "street": item[6],
            "postal_code": item[7],
            "is_default": item[8]
        }
        data[ad].append(address)

    return {"code": 200, "message": "Address created successfully", "data": data}