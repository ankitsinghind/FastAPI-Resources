# FastAPI Course

> Learn to build clear, validated Python APIs with FastAPI, one practical lesson at a time.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-learning-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

This repository is a hands-on FastAPI course. Each lesson contains a small,
runnable example that focuses on one API concept. The examples intentionally
start simple and become more structured as the course progresses.

## Start here

### Requirements

- Python 3.8 or newer
- A terminal and a code editor
- Basic Python knowledge, including functions, dictionaries, and type hints

### Setup

```powershell
git clone https://github.com/ankitsinghind/FASTAPI.git
cd FASTAPI
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install "fastapi[standard]"
```

If PowerShell does not allow activation, run commands with
`.venv\Scripts\python.exe` instead.

### Run a lesson

Every lesson can be run independently:

```powershell
cd "Module_2\L3"
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000/docs> to try the endpoint through FastAPI's
interactive Swagger UI. Stop the server with `Ctrl+C` before starting another
lesson.

## Course roadmap

| Module | Focus | Status |
| --- | --- | --- |
| [Module 1 — Foundations](./Module_1/MODULE_GUIDE.md) | Routes, parameters, request bodies, Pydantic, and CRUD | Available |
| Module 2 — API design | Response models, status codes, and error handling | In progress |
| Module 3 — Persistence | SQL databases, SQLModel, migrations, and repositories | Planned |
| Module 4 — Authentication | Password hashing, JWT, and permissions | Planned |
| Module 5 — Production APIs | Testing, configuration, deployment, and observability | Planned |
| Module 6 — Capstone | Build and ship a complete API | Planned |

## Current lessons

Module 2 currently covers:

- [**Lesson 1 — Response models**](./Module_2/L1/LESSON_GUIDE.md): return only
  the fields that belong in a public API response.
- [**Lesson 2 — Status codes and responses**](./Module_2/L2/LESSON_GUIDE.md):
  use meaningful HTTP status codes and FastAPI's built-in `HTTPException`.
- [**Lesson 3 — Custom errors**](./Module_2/L3/LESSON_GUIDE.md): define an
  application exception and handle it consistently with a global exception
  handler.

Lesson 3 demonstrates that requesting `/users/ankit` returns a successful
response, while another name produces a structured `404` response:

```json
{
  "status": "error",
  "message": "User rohan not found"
}
```

## Learning loop

For each lesson:

1. Read the example and identify the route being demonstrated.
2. Run the application with Uvicorn.
3. Try both successful and failing requests in `/docs`.
4. Change one part of the example and observe the response.
5. Complete a small practice task before moving on.

For the full module descriptions and the detailed learning path, see the
[course guide](./COURSE_GUIDE.md).

## Repository layout

```text
FASTAPI/
├── Module_1/              # Foundations
│   ├── MODULE_GUIDE.md
│   └── L1/ ... L8/
├── Module_2/              # API design
│   ├── MODULE_GUIDE.md
│   ├── L1/                # Response models
│   ├── L2/                # Status codes and HTTPException
│   └── L3/                # Custom exceptions and global handlers
├── COURSE_GUIDE.md        # Detailed course home and standards
└── README.md              # Quick start and course overview
```
