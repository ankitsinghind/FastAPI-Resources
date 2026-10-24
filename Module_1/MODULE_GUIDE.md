# Module 1 · Foundations

Build your first FastAPI endpoints and learn the request/response concepts that every API uses.

## Module outcome

By the end of this module, you will be able to create a small API with typed routes, query and path parameters, validated JSON bodies, nested Pydantic models, and basic CRUD operations.

## Before you begin

- Complete the setup in the [course home](../COURSE_GUIDE.md#start-here).
- Be comfortable reading simple Python functions and dictionaries.
- Keep the server's automatic documentation open at <http://127.0.0.1:8000/docs>.

## Lesson path

| Lesson | Topic | You will practise |
| --- | --- | --- |
| [01 · Your first API](./L1/LESSON_GUIDE.md) | App setup and API vocabulary | Start a server and call a route |
| [02 · Multiple routes](./L2/LESSON_GUIDE.md) | Route decorators | Create a small set of endpoints |
| [03 · Path parameters](./L3/LESSON_GUIDE.md) | Dynamic URL values | Capture and validate an ID |
| [04 · Query parameters](./L4/LESSON_GUIDE.md) | Filtering and defaults | Make an endpoint configurable |
| [05 · Request bodies](./L5/LESSON_GUIDE.md) | POST and Pydantic | Accept structured JSON |
| [06 · Nested models](./L6/LESSON_GUIDE.md) | Composable validation | Model related data |
| [07 · CRUD operations](./L7/LESSON_GUIDE.md) | Create, read, update, delete | Assemble a Todo API |
| [08 · Combined parameters](./L8/LESSON_GUIDE.md) | Path, query, and request body | Combine input sources in one operation |

## Suggested workflow

For each lesson:

1. Read the lesson notes.
2. Run the example with `uvicorn main:app --reload`.
3. Try the endpoint in `/docs`.
4. Complete the practice task.
5. Only then continue to the next lesson.

## Module checkpoint

After Lesson 8, add one field to the Todo model and update the create, read, update, and delete flows to support it. Write down one limitation of the in-memory store that a future module should solve.

## What comes next

Module 2 will turn these fundamentals into a maintainable API by introducing routers, response models, status codes, and explicit error handling.