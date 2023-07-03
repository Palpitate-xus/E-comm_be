from fastapi import APIRouter,UploadFile,File
from models.storemodel.product import Product
from db.database import get_connection, close_connection
from db.db_excel import add_products_from_excel
import shutil
from fastapi import Request
router=APIRouter()
@router.post("/api/suppliers/excel_product")
def upload_products_from_excel(request: Request, file: UploadFile = File(...)):
    token = request.headers.get("Authorization")
    try:
        file_path = f"uploaded_files/{file.filename}"
        print(file_path)
        with open(file_path, "wb") as buffer:
            # 将上传文件对象复制到目标路径
            shutil.copyfileobj(file.file, buffer)
        result = add_products_from_excel(file_path, token)
        if result:
            return {"code": 200, "message": "Successfully add products with excel", "data": {}}
        else:
            return {"message": "Error adding products"}

    except Exception as e:
        return {"message": f"Error uploading file: {e}"}