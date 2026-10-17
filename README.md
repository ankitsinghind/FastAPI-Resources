# FastAPI Resources

A beginner-friendly collection of FastAPI examples, organized as progressive lessons. Each lesson demonstrates one core FastAPI concept using a small, self-contained `main.py` file.

## What you will learn

- Creating a FastAPI application
- Defining GET routes
- Creating multiple routes
- Using dynamic path parameters
- Reading query parameters
- Handling request bodies
- Validating request data with Pydantic models
- Working with nested Pydantic models
- Exploring interactive API documentation

## Prerequisites

- Python 3.8 or later
- A terminal or command prompt
- Basic Python knowledge

## Clone the project

```bash
git clone https://github.com/ankitsinghind/FastAPI-Resources.git
cd FastAPI-Resources
```

## Set up the environment

Create and activate a virtual environment from the project root.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install FastAPI and the standard Uvicorn server:

```bash
pip install "fastapi[standard]"
```

> The original setup notes also mention `uv`, an optional fast Python package and project manager. It is not required to run these examples.

## Run a lesson

Each lesson contains its own `main.py`. Change into the lesson directory and start the development server.

```bash
cd L1
uvicorn main:app --reload
```

Replace `L1` with `L2`, `L3`, `L4`, `L5`, or `L6` to run another lesson.

The server will normally be available at:

- Application: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Stop the server with `Ctrl+C`.

## Project structure

```text
FastAPI-Resources/
├── L1/
│   ├── main.py       # First FastAPI app and root route
│   ├── Readme.md     # Introductory API and route notes
│   ├── setup.txt     # Original setup notes
│   └── FastAPI.png   # FastAPI reference image
├── L2/
│   └── main.py       # Multiple routes
├── L3/
│   └── main.py       # Path parameters
├── L4/
│   └── main.py       # Query parameters
├── L5/
│   └── main.py       # Request body examples
├── L6/
│   └── main.py       # Pydantic and nested models
└── README.md
```

## Lesson guide

### L1 — First FastAPI application

Introduces the `FastAPI` app object and a root GET endpoint:

```python
@app.get("/")
def home():
    return {"message": "hello everyone"}
```

Run it with:

```bash
cd L1
uvicorn main:app --reload
```

Open `/` in a browser, or open `/docs` to try the endpoint interactively.

### L2 — Multiple routes

Defines separate endpoints for a home page, an about page, and a users page:

- `GET /`
- `GET /about`
- `GET /users`

### L3 — Path parameters

Demonstrates dynamic values captured from the URL:

- `GET /users/{user_id}`
- Example: `GET /users/10`

The `user_id: int` annotation enables integer validation.

### L4 — Query parameters

Demonstrates optional, default, and multiple query parameters:

- `GET /users?name=Ankit`
- `GET /products?limit=10`
- `GET /items?name=Book&price=1000`

Query parameters are written after `?` and separated with `&`.

### L5 — Request bodies

Introduces POST requests and data sent from a client to the API. It includes examples using function parameters and a dictionary request body:

- `POST /create-user1`
- `POST /create-user2`

Use the Swagger UI at `/docs` to send JSON requests and inspect responses.

### L6 — Pydantic models

Uses Pydantic `BaseModel` classes for automatic request validation and structured data. It also demonstrates nested models with an address inside a user object:

- `POST /create_user`

Example request body:

```json
{
  "name": "Ankit",
  "address": {
    "city": "Delhi",
    "pin": 110001
  }
}
```

## Recommended learning path

1. Start with `L1` and confirm that the server starts successfully.
2. Use `/docs` after every lesson to test the endpoints.
3. Move to `L2` to understand route definitions.
4. Continue with `L3` and `L4` for URL parameters.
5. Study `L5` for POST requests and request data.
6. Finish with `L6` to learn structured validation with Pydantic.
7. Modify the examples by adding fields, routes, and validation rules.
