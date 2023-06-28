from typing import Optional
from pydantic import BaseModel, Extra

class Supply_order(BaseModel):
    supplier_id:Optional[int]
    product_id:Optional[int]
    stock_quantity:Optional[int]

    class Config:
        extra = Extra.forbid