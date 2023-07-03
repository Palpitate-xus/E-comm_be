from typing import Optional
from pydantic import BaseModel, Extra
from datetime import datetime
import uuid

class Supply_order(BaseModel):
    supplyorder_id:Optional[str]
    supplier_id:Optional[int]
    order_status:Optional[str]
    order_time:Optional[datetime]=datetime.now()

    class Config:
        extra = Extra.forbid