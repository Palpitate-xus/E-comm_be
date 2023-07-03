from fastapi import APIRouter,UploadFile,File
from models.storemodel.product import Product
from db.database import get_connection, close_connection
from db.db_excel import add_products_from_excel

router=APIRouter()
@router.post("/api/suppliers/excel_product")
def upload_products_from_excel(file: UploadFile = File(...)):
    try:
        file_path = f"uploaded_files/{file.filename}"
        print(file_path)
        #print(file_path)
        # with open(file_path, "r") as f:
        #     contents =file.read()
        #     f.write(contents)
        #result=add_products_from_excel(file_path)
        #result =await add_products_from_excel(file_path)
        result = add_products_from_excel(file_path)
        if result:
            return {"code": 200, "message": "Successfully add products with excel", "data": {}}
        else:
            return {"message": "Error adding products"}

    except Exception as e:
        return {"message": f"Error uploading file: {e}"}