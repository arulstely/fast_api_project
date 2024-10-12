from fastapi import FastAPI, HTTPException
from app.schemas import ItemCreate, Item, ClockInCreate, ClockInRecord
from app.crud import (
    create_item, get_item, filter_items, update_item, delete_item,
    create_clock_in, get_clock_in, update_clock_in, delete_clock_in
)

app = FastAPI()

# Items API
@app.post("/items", response_model=Item)
def post_item(item: ItemCreate):
    created_item = create_item(item)
    created_item['id'] = str(created_item['_id'])
    created_item.pop('_id') 
    return created_item

@app.get("/items/{item_id}", response_model=Item)
def get_item_by_id(item_id: str):
    item = get_item(item_id)  
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item['id'] = str(item['_id'])  
    item.pop('_id')  

    return item

@app.get("/items/filter")
def filter_items_api(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    filters = {}
    if email:
        filters['email'] = email
    if expiry_date:
        filters['expiry_date'] = expiry_date
    if insert_date:
        filters['insert_date'] = insert_date
    if quantity:
        filters['quantity'] = {'$gte': quantity}  
    return filter_items(filters)

@app.delete("/items/{item_id}")
def delete_item_api(item_id: str):
    delete_item(item_id)

@app.put("/items/{item_id}")
def update_item_api(item_id: str, item: ItemCreate):
    update_item(item_id, item)

# Clock-In Records API
@app.post("/clock-in", response_model=ClockInRecord)
def post_clock_in(clock_in: ClockInCreate):
    created_clock_in = create_clock_in(clock_in)
    created_clock_in['id'] = str(created_clock_in['_id'])  
    created_clock_in.pop('_id')  
    return created_clock_in

@app.get("/clock-in/{clock_in_id}", response_model=ClockInRecord)
def get_clock_in_by_id(clock_in_id: str):
    clock_in = get_clock_in(clock_in_id)
    if clock_in is None:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    clock_in['id'] = str(clock_in['_id'])  
    clock_in.pop('_id')  
    return clock_in

@app.delete("/clock-in/{clock_in_id}")
def delete_clock_in_api(clock_in_id: str):
    delete_clock_in(clock_in_id)

@app.put("/clock-in/{clock_in_id}")
def update_clock_in_api(clock_in_id: str, clock_in: ClockInCreate):
    update_clock_in(clock_in_id, clock_in)
