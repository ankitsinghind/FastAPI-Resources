# Lesson 1 · Your first API

**Goal:** understand what an API, route, and FastAPI application are, then run your first endpoint.

## Key ideas

- An API is a bridge between a client (such as a browser or frontend) and a backend.
- A route is a URL path connected to a Python function.
- `GET` is commonly used to fetch data.
- FastAPI generates interactive documentation for your routes.

## Run it

From this folder:

```powershell
uvicorn main:app --reload
```

Visit:

- <http://127.0.0.1:8000/> for the response;
- <http://127.0.0.1:8000/docs> for interactive API documentation.

## Practice

Change the response message, restart if needed, and call the endpoint again. Then add a second GET route of your own.

**Next:** [Lesson 2 — Multiple routes](../L2/LESSON_GUIDE.md)
