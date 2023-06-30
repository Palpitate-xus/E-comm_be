from typing import Optional
from pydantic import BaseModel, Extra

class Userinfo(BaseModel):
    Authorization: Optional[str]
    class Config:
        extra = Extra.forbid