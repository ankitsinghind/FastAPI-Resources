#Query Parameter- used to filter
#/users?name=ankit
#/users?price=1000

from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name: str=None): #Optional parameters
    return {"Name":name}

@app.get("/products")
def get_users(limit: int = 10): #Default parameters
    return {"Limit":limit}

@app.get("/items")
def get_users(name: str = None, price: int = 0): #Multiple queries
    return {
        "name":name,
        "price":price-price/10
    }