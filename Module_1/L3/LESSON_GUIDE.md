# Lesson 3 · Path parameters

**Goal:** capture a value from a URL and let FastAPI validate its type.

## Key ideas

A path parameter makes a route dynamic:

```text
/users/1
/users/2
```

The `{user_id}` placeholder is passed to the function. Annotating it as `int` means FastAPI validates the incoming value and reports a useful error for invalid input.

## Run it

```powershell
uvicorn main:app --reload
```

Try `/users/42`, then try `/users/not-a-number` and inspect the validation response.

## Practice

Add a `/products/{product_id}` route with an integer ID. Return the ID in the response and test both a valid and invalid value.

**Next:** [Lesson 4 — Query parameters](../L4/LESSON_GUIDE.md)
