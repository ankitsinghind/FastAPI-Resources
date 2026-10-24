# Lesson 4 · Query parameters

**Goal:** use optional, default, and multiple query parameters to control a response.

## Key ideas

Query parameters follow a `?` in the URL:

```text
/users?name=ankit
/products?limit=10
```

FastAPI reads function parameters that are not part of the path as query parameters. Type annotations and defaults describe what the client may send.

## Run it

```powershell
uvicorn main:app --reload
```

Try the examples in `/docs`, or call:

- `/users?name=Ankit`
- `/products?limit=5`
- `/items?name=Book&price=100`

## Practice

Add a `category` query parameter to `/items`. Give it a useful default and return it in the response.

**Next:** [Lesson 5 — Request bodies](../L5/LESSON_GUIDE.md)
