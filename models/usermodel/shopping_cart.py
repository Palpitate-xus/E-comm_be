from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ShoppingCart(BaseModel):
    user_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    add_time: Optional[datetime] = datetime.now()
