from typing import Optional
from pydantic import BaseModel, Extra

class Supplier(BaseModel):
    supplier_id: Optional[int]
    supplier_name: Optional[str]
    contact_info: Optional[str]
    supplier_address: Optional[str]
    user_id: Optional[int]
    '''
    class Config:
        extra = Extra.forbid'''