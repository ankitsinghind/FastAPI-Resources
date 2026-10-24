# FastAPI from First Principles

> A practical, project-based course for building clear, validated Python APIs with FastAPI.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-learning-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Course status](https://img.shields.io/badge/status-in%20progress-F59E0B)](https://github.com/ankitsinghind/FASTAPI)

This repository is a structured FastAPI course. Each module introduces one layer of API development, and each lesson includes a runnable example, a focused concept, and a small practice task. The course will grow over time—new modules will be added without changing the learning path that is already here.

## Start here

### 1. Check your tools

- Python **3.8 or newer**
- A terminal
- A code editor such as VS Code
- Basic Python knowledge: functions, lists, dictionaries, and type hints

### 2. Clone and enter the course

```powershell
https://github.com/ankitsinghind/.git
cd FastAPI-Resources
```

### 3. Create an environment and install FastAPI

```powershell
python -m venv .venv
.venv\Scripts\Activate
python -m pip install "fastapi[standard]"
```

### 4. Follow the path

Start with the [course roadmap](#course-roadmap), then open [Module 1](./Module_1/MODULE_GUIDE.md). Work through the lessons in order. Every lesson is independent enough to run on its own, but the sequence is intentional.

## Course roadmap

| Module | Focus | Status |
| --- | --- | --- |
| [01 · Foundations](./Module_1/MODULE_GUIDE.md) | Routes, parameters, request bodies, Pydantic, and CRUD | **Available** |
| [02 · API design](./Module_2/MODULE_GUIDE.md) | Response models, status codes, and error handling | **In progress** |
| 03 · Persistence | SQL databases, SQLModel, migrations, and repository patterns | Coming soon |
| 04 · Authentication | Users, password hashing, JWT, and permissions | Coming soon |
| 05 · Production APIs | Testing, configuration, documentation, deployment, and observability | Coming soon |
| 06 · Capstone | Build and ship a complete production-style API | Coming soon |

## What you will build

By the end of Module 1, you will be able to:

- create a FastAPI application and run it locally;
- define clear GET, POST, PUT, and DELETE endpoints;
- capture path and query parameters with type validation;
- accept JSON request bodies with Pydantic models;
- compose nested data models;
- build a small in-memory Todo API and explore it through automatic docs.

## Learning loop

Use the same loop for every lesson:

1. **Preview** the lesson guide and its outcome.
2. **Run** the example before changing it.
3. **Inspect** `/docs` and make a request.
4. **Modify** one thing and observe the result.
5. **Complete** the practice task before moving on.

This is a hands-on course: reading the example is useful, but typing and testing the change is where the learning happens.

## Repository map

```text
FASTAPI/
├── Module_1/
│   ├── MODULE_GUIDE.md    # Module overview and progress checklist
│   ├── L1/                # First app and API vocabulary
│   ├── L2/                # Multiple routes
│   ├── L3/                # Path parameters
│   ├── L4/                # Query parameters
│   ├── L5/                # Request bodies and Pydantic
│   ├── L6/                # Nested models and validation
│   ├── L7/                # CRUD Todo API
│   └── L8/                # Combined path, query, and body parameters
├── README.md              # Quick course overview
```

Each lesson folder contains the runnable Python example. Lesson notes live beside the example so that the code and explanation stay together.

## Running a lesson

Open a lesson folder, then start its `main.py`:

```powershell
cd "Module_1\L1"
uvicorn main:app --reload
```

Open <http://127.0.0.1:8000/docs> to use Swagger UI. Stop the server with `Ctrl+C` before starting another lesson. Replace `L1` with the lesson you want to practise. Each lesson's `LESSON_GUIDE.md` explains its goal and practice task.

## Progress checklist

- [x] Module 1 — Foundations
- [ ] Module 2 — API design
- [ ] Module 3 — Persistence
- [ ] Module 4 — Authentication
- [ ] Module 5 — Production APIs
- [ ] Module 6 — Capstone

## Course standards

Examples favour clarity over cleverness. As the course advances, examples will evolve toward production practices such as typed response models, explicit HTTP errors, tests, environment-based configuration, and a database. Earlier lessons intentionally keep infrastructure small so the underlying FastAPI concepts remain visible.
