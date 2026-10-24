# Lesson 5 · Request bodies and Pydantic

**Goal:** accept structured JSON in a POST request and validate it with a Pydantic model.

## Key ideas

- `GET` commonly reads data; `POST` commonly creates data.
- A request body carries structured data from the client to the server.
- A Pydantic `BaseModel` describes the expected fields and types.
- FastAPI uses that model to validate input and document the request schema.

The lesson contains a simple body example and a `User` model. Compare them in `/docs` and notice how the model gives the API a precise contract.

## Run it

```powershell
uvicorn main:app --reload
```

Use Swagger UI to send a valid user, then remove a required field or change a type to see validation in action.

## Practice

Create a `Product` model with `name` and `price`, then add a POST endpoint that returns the validated product.

**Next:** [Lesson 6 — Nested models](../L6/LESSON_GUIDE.md)
