#Request Body- Data sent by cient to backend. eg. signup, create a insta post, add a product in cart.
#Sent in JSON format. POST request is used.

#GET - fetch
#POST - create

from fastapi import FastAPI

app = FastAPI()


@app.post("/create-user1")
def create_user(name:str, age:int):
    return{
        "name":name,
        "age":age
    }

@app.post("/create-user2")
def create_user(user:dict):
    return{
        "message":"User Created",
        "data":user
    }
