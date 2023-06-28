from datetime import datetime
from typing import Optional
from pydantic import BaseModel,Extra

class Orders(BaseModel):
    order_id: Optional[str]
    user_id: Optional[int]
    order_status: Optional[str]
    total_amount: Optional[float]
    order_time: Optional[datetime] = datetime.now()
    payment_status: Optional[str]
    payment_method: Optional[str]
    shipping_address: Optional[str]

    class Config:
        extra = Extra.forbid