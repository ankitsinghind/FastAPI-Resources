#Path parameters allows to capture dynamic values from URL ie. Dynamic Routes
'''
/users/1
/users/2
'''

from fastapi import FastAPI

app = FastAPI()
@app.get("/users/{user_id}")
def get_users(user_id:int): #Type validation
    return {"user_id":user_id}
