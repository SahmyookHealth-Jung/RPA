from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "hi"}

@app.get("/item")
async def read_item(item_id : int, name: str = None, age : int =0):
    return {"item_id": item_id, "name" : name, "age" : age}

@app.get("/user")
async def read_user(name : str = None, studentcode:int =0, major:str=None):
    return{"msg: ": major , name : studentcode }