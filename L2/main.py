#Multiple Routes
from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message":"I am home page"}

#About Route
@app.get("/about")
def about():
    return {"message":"I am about page"}

#User Route
@app.get("/users")
def users():
    return{
        "users": ["Ankit", "Shivansh", "Shweta"]
    }