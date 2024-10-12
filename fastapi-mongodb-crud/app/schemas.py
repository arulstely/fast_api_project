from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: str  # YYYY-MM-DD

class Item(ItemCreate):
    id: str
    insert_date: datetime

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInRecord(ClockInCreate):
    id: str
    insert_datetime: datetime
