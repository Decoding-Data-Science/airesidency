#step 1
#pip install fastapi 
#pip install  uvicorn

#step 2 
#run in terminal uvicorn main:app --reload 

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI
from typing import Union

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, Ritesh'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To DDS  Youtube Channel': f'{name}'}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}







