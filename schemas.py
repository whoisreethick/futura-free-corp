from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    name: str
    content: str

class MessageResponse(BaseModel):
    id: int
    name: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True