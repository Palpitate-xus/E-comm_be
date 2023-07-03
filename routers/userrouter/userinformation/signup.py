from fastapi import APIRouter
from models.suppliermodel.suser import SUser
from db import db_user

router = APIRouter()


@router.post("/api/users/register/")
def register_user(suser: SUser):
    if suser.user_type == 'supplier':
        db_user.create_user1(suser)
    else:
        db_user.create_user(suser)

    return {"code": 200, "message": "User account created successfully", "data": {}}


