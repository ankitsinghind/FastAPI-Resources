from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Automatic type validation
try:
    user = User(name="Alice", age="25")  # age is string, will be converted to int
    print(user)
except Exception as e:
    print("Error:", e)

#Output : name='Alice' age=25  # age converted to int automatically