from sqlmodel import SQLModel, Field
from typing import Optional

class BaseUser(SQLModel):
    name: str
    email: str
    profile_pic: str
    user_type_id: int
    
    
class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class CreateUser(BaseUser):
    profile_pic: Optional[str] = None
    pass

class UpdateUser(BaseUser):
    name: Optional[str] = None
    email: Optional[str] = None
    profile_pic: Optional[str] = None
    user_type_id: Optional[int] = None

class ReadUser(BaseUser):
    id: int
