#Pydantic - automatic data validation

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data": user
    }
"""

class Address(BaseModel):
    city:str
    pin:int

class User(BaseModel):
    name:str
    address:Address #Nested Models

@app.post("/create_user")
def create_user(user:User):
    return user