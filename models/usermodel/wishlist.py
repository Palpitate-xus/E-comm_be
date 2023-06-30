from datetime import datetime
from pydantic import BaseModel,Extra
from typing import Optional

class Wishlist(BaseModel):
    wish_id: Optional[int]
    product_id: Optional[int]
    user_id: Optional[int]
    add_time: Optional[datetime] = datetime.now()
    class Config:
        extra = Extra.forbid