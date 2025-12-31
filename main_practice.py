from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

#Create fastapi app instance
app = FastAPI()

#1. simple get endpoint
@app.get("/")
def home():
    return {"message": "Hello World"}

#2. another get endponit
@app.get("/ping")
def ping():
    return {"message": "pong"}

#3.define a data model for post requestes
class Item(BaseModel):
    name: str
    price: float
    
#4. post endpoints(accepts JSON data)
@app.post("/items/")
def create_item(item: Item):
    return {"item_created": item}
