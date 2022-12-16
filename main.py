from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
my_awesome_api = FastAPI()
# @app.post()
# @app.put()
# @app.delete()

# @app.options()
# @app.head()
# @app.patch()
# @app.trace()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# @my_awesome_api.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Path Parameters start here


@my_awesome_api.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# @my_awesome_api.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


@my_awesome_api.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@my_awesome_api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}

#Path Parameters

# @my_awesome_api.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

#Path parameters with types

# @my_awesome_api.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


@my_awesome_api.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@my_awesome_api.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@my_awesome_api.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@my_awesome_api.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

#Path parameters end here

#Query parameters start here

@my_awesome_api.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@my_awesome_api.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
#Query parameters end here


#Request Body starts here
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
@my_awesome_api.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
    
#Request Body ends here