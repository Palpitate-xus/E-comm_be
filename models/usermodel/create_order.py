from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class OrderDetail(BaseModel):
    product_id: Optional[int]
    quantity: Optional[int]
    product_price: Optional[float]

class CreateOrder(BaseModel):
    user_id: Optional[int]
    order_details: Optional[List[OrderDetail]]
    order_status: Optional[str] = 'Pending'
    total_amount: Optional[float]
    order_time: Optional[datetime] = datetime.now()
    payment_status: Optional[str] = 'unpaid'
    shipping_address: Optional[str]

