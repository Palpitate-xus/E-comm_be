from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/api/users/logout/")
async def logout():
    return {"code": 200, "msg": "success"}