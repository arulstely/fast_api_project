from app.database import db
from app.schemas import ItemCreate, ClockInCreate
from bson import ObjectId
from datetime import datetime

# Items CRUD
def create_item(item: ItemCreate):
    item_data = item.dict()
    item_data['insert_date'] = datetime.utcnow()
    result = db.items.insert_one(item_data)
    return {**item_data, "id": str(result.inserted_id)}

def get_item(item_id: str):
    return db.items.find_one({"_id": ObjectId(item_id)})

def filter_items(filters: dict):
    query = {}
    if 'email' in filters:
        query['email'] = filters['email']
    if 'expiry_date' in filters:
        query['expiry_date'] = {'$gt': filters['expiry_date']}
    if 'insert_date' in filters:
        query['insert_date'] = {'$gt': filters['insert_date']}
    if 'quantity' in filters:
        query['quantity'] = {'$gte': filters['quantity']}
    return list(db.items.find(query))

def update_item(item_id: str, item: ItemCreate):
    db.items.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict(exclude={'insert_date'})})

def delete_item(item_id: str):
    db.items.delete_one({"_id": ObjectId(item_id)})

# Clock-In Records CRUD
def create_clock_in(clock_in: ClockInCreate):
    clock_in_data = clock_in.dict()
    clock_in_data['insert_datetime'] = datetime.utcnow()
    result = db.clock_in_records.insert_one(clock_in_data)
    return {**clock_in_data, "id": str(result.inserted_id)}

def get_clock_in(clock_in_id: str):
    return db.clock_in_records.find_one({"_id": ObjectId(clock_in_id)})

def update_clock_in(clock_in_id: str, clock_in: ClockInCreate):
    db.clock_in_records.update_one({"_id": ObjectId(clock_in_id)}, {"$set": clock_in.dict(exclude={'insert_datetime'})})

def delete_clock_in(clock_in_id: str):
    db.clock_in_records.delete_one({"_id": ObjectId(clock_in_id)})
