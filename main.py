# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to Dear Name 💌"}

# @app.get("/messages/{name}")
# def get_messages(name: str):
#     return {"name": name, "messages": f"Fetching messages for {name}..."}

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Dear Name 💌"}

@app.post("/messages/", response_model=schemas.MessageResponse)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(
        name=message.name.strip().lower(),
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/messages/{name}", response_model=List[schemas.MessageResponse])
def get_messages(name: str, db: Session = Depends(get_db)):
    messages = db.query(models.Message)\
        .filter(models.Message.name == name.strip().lower())\
        .all()
    if not messages:
        raise HTTPException(status_code=404, detail=f"No messages found for {name}")
    return messages