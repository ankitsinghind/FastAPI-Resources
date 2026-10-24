# Lesson 8 · Combined parameters

**Goal:** combine path parameters, query parameters, and a request body in one operation.

## Key ideas

An endpoint can receive different kinds of input at the same time:

- the path identifies the resource;
- the request body carries structured data;
- the query string controls an option such as whether to notify a client.

FastAPI uses the function signature and type annotations to validate each source and document it separately in `/docs`.

## Run it

```powershell
uvicorn main:app --reload
```

Try `PUT /users/101?notify=true` with this body:

```json
{
  "name": "Ankit",
  "age": 24
}
```

## Practice

Change the update behavior so it reports a clear response when the requested user does not exist. Test both `notify=true` and the default `notify=false`.

**Next:** return to the [Module 1 overview](../MODULE_GUIDE.md).
