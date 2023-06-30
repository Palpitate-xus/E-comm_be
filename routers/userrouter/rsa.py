from fastapi import APIRouter
from models.usermodel.wishlist import Wishlist
from db import db_user
from fastapi import Request
router = APIRouter()


@router.post("/api/publicKey")
def rsa():
    return {"code": 200, "msg": 'success', "data": {"mockServer": "true", "publicKey":'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBT2vr+dhZElF73FJ6xiP181txKWUSNLPQQlid6DUJhGAOZblluafIdLmnUyKE8mMHhT3R+Ib3ssZcJku6Hn72yHYj/qPkCGFv0eFo7G+GJfDIUeDyalBN0QsuiE/XzPHJBuJDfRArOiWvH0BXOv5kpeXSXM8yTt5Na1jAYSiQ/wIDAQAB'}
}