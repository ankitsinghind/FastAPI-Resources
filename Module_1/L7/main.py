# CRUD operations : Create API, Read API, Update API, Delete API

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todo_store =[]

class Todo_class(BaseModel):
    id:int
    title:str
    completed:bool

#Create API
@app.post("/todos")
def create_todo(todo: Todo_class):
    todo_store.append(todo)
    return {"message": "TODO added", "data": todo}


#Read API
@app.get("/todos")
def read_todo():
    return todo_store

#---------------------------------------------------------------
#Using Path Parameter to read only by id

@app.get("/todos/{todos_id}")
def read_todo_id(todos_id:int):
    for todo in todo_store:
        if todo.id == todos_id:
            return todo
    return {"error": "TODO NOT FOUND"}


#Update API
@app.put("/todos/{todos_id}")
def update_todo(todos_id:int, updated_todo: Todo_class):
    for index, todo in enumerate(todo_store):
        if todo.id == todos_id:
            todo_store[index] = updated_todo
            return {
                "message": "TODO UPDATED",
                "data": updated_todo
            }
    return {"error": "TODO NOT FOUND"}

#Delete API
@app.delete("/todos/{todos_id}")
def detete_todo(todos_id:int):
    for index, todo in enumerate(todo_store):
        if todo.id == todos_id:
            todo_store.pop(index)
            return {"message": "TODO DELETED"}
    return {"error": "TODO NOT FOUND"}