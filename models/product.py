from typing import Optional
from pydantic import BaseModel, Extra

class Product(BaseModel):
    product_id: Optional[int]
    product_name: Optional[str]
    product_description: Optional[str]
    product_price: Optional[float]
    category_id: Optional[int]
    stock_quantity: Optional[int]
    product_image: Optional[str]
    '''
    class Config:
        extra = Extra.forbid'''