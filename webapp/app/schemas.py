from pydantic import BaseModel
from datetime import datetime



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

