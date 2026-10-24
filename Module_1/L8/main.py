# Path + Query + Request Body

'''
PUT /users/101?notify=true
{
    "name" : "Ankit"
    "age" : 24
}
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message" : "User Created",
        "data" : user
    }

@app.put("/users/{user_id}")
def updated_user(user_id:int, user:User, notify:bool = False):
    if user_id < len(users):
        users[user_id] = user

        return{
            "message" : "User Updated",
            "notify" : notify,
            "data" : user
        }

@app.get("/")
def get_user():
    return users