# Lesson 7 · CRUD checkpoint

**Goal:** combine the module's concepts into a small Todo API.

## Key ideas

CRUD describes the four basic data operations:

| Operation | HTTP method | Endpoint |
| --- | --- | --- |
| Create | `POST` | `/todos` |
| Read all | `GET` | `/todos` |
| Read one | `GET` | `/todos/{todos_id}` |
| Update | `PUT` | `/todos/{todos_id}` |
| Delete | `DELETE` | `/todos/{todos_id}` |

This example stores data in a Python list, so it is intentionally a learning project. Restarting the server clears the data.

## Run it

```powershell
uvicorn main:app --reload
```

Use `/docs` to create a Todo first, then read, update, and delete it by ID.

## Practice

Add a `priority` field to `Todo_class`. Update the model and try every CRUD operation with the new field.

## Checkpoint reflection

Before moving on, answer:

1. Which values come from the path, query string, and request body?
2. Where does validation happen?
3. What would happen to the Todo list if the server restarted?

**Next:** [Lesson 8 — Combined parameters](../L8/LESSON_GUIDE.md)
