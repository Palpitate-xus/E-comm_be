from typing import Optional
from pydantic import BaseModel, Extra

class Product(BaseModel):
    product_id: Optional[int]
    product_name: Optional[str]
    product_description: Optional[str]
    product_price: Optional[float]
    category: Optional[str]
    stock_quantity: Optional[int]
    product_image: Optional[str]
    product_status: Optional[str]
    class Config:
        extra = Extra.forbid