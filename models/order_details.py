from typing import Optional
from pydantic import BaseModel,Extra

class OrderDetail(BaseModel):
    order_id: Optional[str]
    product_id: Optional[int]
    quantity: Optional[int]
    unit_price: Optional[float]
    class Config:
        extra = Extra.forbid

