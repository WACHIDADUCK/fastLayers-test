from sqlmodel import SQLModel, Field
from typing import Optional

class BaseLesson(SQLModel):
    title: str
    start_time: str
    end_time: str
    subject: str

class Lesson(BaseLesson, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class CreateLesson(BaseLesson):
    pass

class UpdateLesson(BaseLesson):
    title: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    subject: Optional[str] = None

class ReadLesson(BaseLesson):
    id: int
