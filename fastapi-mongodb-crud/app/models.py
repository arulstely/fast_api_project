from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: str

class Item(ItemCreate):
    id: str  # This will hold the converted ObjectId

class ClockInCreate(BaseModel):
    email: str
    location: str

class ClockInRecord(ClockInCreate):
    id: str  # This will hold the converted ObjectId
    insert_date: str  # This can be a datetime string in your desired format
