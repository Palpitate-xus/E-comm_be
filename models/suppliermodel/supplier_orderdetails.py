from typing import Optional
from pydantic import BaseModel, Extra
from datetime import datetime
import uuid

class Supply_orderdetails(BaseModel):
    supplyorder_id:Optional[str]
    product_id:Optional[int]
    quantity:Optional[str]
    product_name:Optional[str]

    class Config:
        extra = Extra.forbid