from typing import Optional
from pydantic import BaseModel,Extra
from datetime import datetime

class Inventory(BaseModel):
    supplier_id:Optional[int]
    product_id:Optional[str]
    inventory_time:Optional[datetime]=datetime.now()
    inventory_num:Optional[int]
    class Config:
        extra = Extra.forbid