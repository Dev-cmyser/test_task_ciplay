from pydantic import BaseModel
from datetime import datetime

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True


class Event(BaseModel):
    id: int
    date: datetime
    views: int
    clicks: int
    cost: float

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    date: datetime
    views: int
    clicks: int
    cost: float

