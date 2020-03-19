'''
Jackson Frank
FastAPI Example Project
main.py: Provides Structure of API
'''

from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return{ "message": "Hello World" }

'''
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id" : item_id}
'''

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

'''
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazying item that has a long desription"}
        )
    return item
'''

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long desription"}
        )
    return item

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return {"item_id": item_id, **item_dict}

'''
@app.get("/items/")
async def read_items(
    q: str = Query(
        None, 
        title="Query String", 
        description = "Query string for the items to search in the database that have a good match", 
        max_length=50, 
        regex = "^fixedquery$",
        alias = "item-query",
        deprecated = True
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''

