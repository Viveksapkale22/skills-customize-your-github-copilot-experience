from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

# In-memory store: id -> Item
items: Dict[int, Item] = {}
next_id = 1

@app.get("/items/")
def list_items():
    return list(items.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/", status_code=201)
def create_item(payload: Item):
    global next_id
    item = Item(id=next_id, name=payload.name, description=payload.description)
    items[next_id] = item
    next_id += 1
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, payload: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, name=payload.name, description=payload.description)
    items[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None
