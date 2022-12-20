import models
import schemas
from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()



@app.post("/create_event", response_model=schemas.Event, status_code=status.HTTP_201_CREATED)
def create_todo(event: schemas.EventCreate, session: Session = Depends(get_session)):

    # create an instance of the ToDo database model
    eventdb = models.Event(cost = event.cost, clicks = event.clicks, views = event.views, date = event.date)

    # add it to the session and commit it
    session.add(eventdb)
    session.commit()
    session.refresh(eventdb)

    # return the todo object
    return eventdb



@app.delete("/delete_all_events/", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(session: Session = Depends(get_session)):

    # get the todo item with the given id
    events = session.query(models.Event).all()

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if events:
        for event in events:
            session.delete(event)
            session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"not found events ")

    return None
# http://127.0.0.1:8000/?start=2022-12-20T20:01:56.083000&end=2022-12-20T20:01:56.083000
@app.get("/", response_model = List)
def get_event_list(start: datetime | None = '2022-12-20T20:01:56.083000', end: datetime | None = '2022-12-20T20:01:56.083000', session: Session = Depends(get_session)):
    

        
    # get all todo items
    event_list = session.query(models.Event).all()
    
    event_list = sorted(
    event_list,
    key=lambda x: datetime.strptime(str(x.date)[:-7], '%Y-%m-%d %H:%M:%S'), reverse=False
)   
    events = []
    for i in event_list:
        if i.clicks == 0 or i.cost == 0:
            cpc = 0
        if i.views == 0 or i.cost == 0:
            cpm = 0
        events.append({
            'id': i.id,
            'date': i.date,
            'views': i.views,
            'clicks': i.clicks,
            'cost': i.cost,
            'cpc': cpc,
            'cpm': cpm

        })
    event_list = []
    if start and end:
        start = datetime.strptime(str(start)[:-7], '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(str(end)[:-7], '%Y-%m-%d %H:%M:%S')
        for i in events:
            if start <= datetime.strptime(str(i['date'])[:-7], '%Y-%m-%d %H:%M:%S') <= end:
                event_list.append(i)
        
        return event_list
    return events



