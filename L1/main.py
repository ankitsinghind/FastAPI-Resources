from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello everyone"}

# run server by: uvicorn main:app --reload

##check url on postman and in browser add /docs and show