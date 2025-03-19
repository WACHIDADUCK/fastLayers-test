from sqlmodel import SQLModel, Field
from typing import Optional

class BaseUserType(SQLModel):
    name: str

class UserType(BaseUserType, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class CreateUserType(BaseUserType):
    pass

class UpdateUserType(BaseUserType):
    name: Optional[str] = None

class ReadUserType(BaseUserType):
    id: int
