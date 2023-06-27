from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    user_id: Optional[int]
    username: Optional[str]
    password: Optional[str]
    email: Optional[str]
    user_type: Optional[str]
    registration_date: Optional[datetime] = datetime.now()
    last_login_date: Optional[datetime] = datetime.now()
    user_status: Optional[str] = 'active'



