# Lesson 6 · Nested models

**Goal:** model related JSON objects with nested Pydantic models.

## Key ideas

Real API payloads are often hierarchical. A `User` can contain an `Address`, and the `Address` can have its own validated fields. Composing models keeps each part of the contract explicit and reusable.

## Run it

```powershell
uvicorn main:app --reload
```

Send a payload shaped like:

```json
{
  "name": "Ankit",
  "address": {
    "city": "Delhi",
    "pin": 110001
  }
}
```

Then change `pin` to an invalid value and inspect the validation details.

## Practice

Add an `email` field to the user model and test both a complete and incomplete request.

**Next:** [Lesson 7 — CRUD checkpoint](../L7/LESSON_GUIDE.md)
