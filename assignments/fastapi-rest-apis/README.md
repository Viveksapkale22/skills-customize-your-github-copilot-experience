# 🛠️ Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using the FastAPI framework that exposes CRUD endpoints for a simple resource (e.g., `Item`). Students will practice request/response modeling, routing, and basic in-memory data storage.

## 📝 Tasks

### 🛠️ Task 1 — Core API

#### Description

Implement a FastAPI application with endpoints to create, read, update, and delete `Item` resources.

#### Requirements

- Implement the following endpoints:
  - `GET /items/` — list all items
  - `GET /items/{item_id}` — get a single item by id
  - `POST /items/` — create a new item (accepts JSON body)
  - `PUT /items/{item_id}` — update an existing item
  - `DELETE /items/{item_id}` — delete an item
- Use Pydantic models for request and response validation.
- Maintain items in-memory (e.g., a dictionary) — persistence is not required.

### 🛠️ Task 2 — Input validation & errors

#### Description

Add input validation and appropriate HTTP error responses.

#### Requirements

- Validate request payloads with Pydantic (required fields, types).
- Return `404` for missing items and `400` for invalid input when appropriate.

### 🛠️ Task 3 — (Optional) Extras

#### Description

Add optional enhancements for more advanced students.

#### Requirements

- Add query parameters for filtering or pagination.
- Add simple authentication (e.g., API key header) or CORS configuration.

## 📦 Files included

- `starter-code.py` — minimal FastAPI app scaffolding
- `requirements.txt` — dependencies for running the app

## 🚀 How to run

1. Create and activate a virtual environment (recommended).

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app with Uvicorn:

```bash
uvicorn starter-code:app --reload --port 8000
```

4. Open `http://127.0.0.1:8000/docs` to view interactive API docs.

## 🎓 Learning outcomes

- Design and implement REST endpoints with FastAPI.
- Use Pydantic models for validation and clear response schemas.
- Understand HTTP methods and status codes for CRUD operations.

## Grading / Acceptance

The assignment is complete when all endpoints work as specified and the API validates input and returns proper HTTP status codes.
