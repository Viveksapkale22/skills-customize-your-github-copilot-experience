# 🛠️ Assignment: Building Persistent APIs with FastAPI + SQLite

## 🎯 Objective

Extend FastAPI skills by building a REST API that stores data persistently in a SQLite database using `SQLModel` (or `SQLAlchemy`). Students will implement CRUD operations, request validation, and basic error handling.

## 📝 Tasks

### 🛠️ Task 1 — Persistent CRUD API

#### Description

Implement a FastAPI application with persistent storage for an `Item` resource using SQLite.

#### Requirements

- Endpoints:
  - `GET /items/` — list all items
  - `GET /items/{item_id}` — get a single item
  - `POST /items/` — create an item
  - `PUT /items/{item_id}` — update an item
  - `DELETE /items/{item_id}` — delete an item
- Use Pydantic/SQLModel models for validation and schema generation.
- Persist data in a SQLite database file (created automatically).
- Return appropriate HTTP status codes (`201`, `404`, `400`, `204`).

### 🛠️ Task 2 — Validation & Error Handling

#### Description

Add validation and clear error responses for invalid input and missing resources.

#### Requirements

- Validate payloads using models; return `400` for invalid input.
- Return `404` when an item is not found.

### 🛠️ Task 3 — (Optional) Extras

#### Description

Add features for more advanced learning.

#### Requirements

- Add query filters or pagination.
- Add a small authentication layer (API key) or CORS config.
- Provide a migration strategy or a simple script to reset the DB.

## 📦 Files included

- `starter-code.py` — FastAPI app scaffold using `SQLModel` and SQLite
- `requirements.txt` — dependencies to run the app

## 🚀 How to run

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn starter-code:app --reload --port 8000
```

4. Visit `http://127.0.0.1:8000/docs` for interactive API docs.

## 🎓 Learning outcomes

- Implement persistent CRUD APIs with FastAPI and SQLite.
- Use SQLModel (Pydantic + SQLAlchemy) models for validation and persistence.
- Handle common API errors and status codes.

## Grading / Acceptance

Complete when all endpoints work, validations are enforced, and the API persists data in `fastapi_persistence.db` without runtime errors.
