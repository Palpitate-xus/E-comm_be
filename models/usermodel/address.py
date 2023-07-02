from typing import Optional
from pydantic import BaseModel

class Address(BaseModel):
    address_id: Optional[int]
    user_id: Optional[int]
    recipient_name: Optional[str]
    phone_number: Optional[str]
    province: Optional[str]
    city: Optional[str]
    street: Optional[str]
    postal_code: Optional[str]
    is_default: Optional[bool]

