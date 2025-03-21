from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.v1.models.user_type import UserType 

class BaseUser(SQLModel):
    name: str
    email: str
    profile_pic: str
    user_type_id: int

class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_type_id: Optional[int] = Field(default=None, foreign_key="usertype.id")

    # Relationship to UserType
    user_type: Optional["UserType"] = Relationship(back_populates="users")

class CreateUser(BaseUser):
    profile_pic: Optional[str] = None

class UpdateUser(BaseUser):
    name: Optional[str] = None
    email: Optional[str] = None
    profile_pic: Optional[str] = None
    user_type_id: Optional[int] = None

class ReadUser(BaseUser):
    id: int