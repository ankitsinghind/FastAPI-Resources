# Lesson 2 · Multiple routes

**Goal:** define several endpoints in one FastAPI application.

## Key ideas

`@app.get(...)` maps a URL path to a function. A useful API is a collection of focused routes, not one large function.

This example includes home, about, and users endpoints. Run it and inspect all three operations in `/docs`.

## Run it

```powershell
uvicorn main:app --reload
```

Try:

- `GET /`
- `GET /about`
- `GET /users`

## Practice

Add a `/health` route that returns a small JSON object such as `{"status": "ok"}`. Confirm it appears in Swagger UI.

**Next:** [Lesson 3 — Path parameters](../L3/LESSON_GUIDE.md)
