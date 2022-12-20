from sqlalchemy import Column, Integer, String, Numeric, DateTime, Sequence
from database import Base
from datetime import datetime




class Event(Base):
    __tablename__ = 'my'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    views = Column(Integer, Sequence("", optional=True))
    clicks = Column(Integer, Sequence("", optional=True))
    cost = Column(Integer, Sequence("", optional=True))