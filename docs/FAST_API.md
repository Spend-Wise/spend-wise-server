# FastAPI Documentation for Spend Wise Server

## 1. What is FastAPI?
FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+ based on standard Python type hints. It sits on top of Starlette (for the web parts) and Pydantic (for data validation and settings management). Its design goals are developer productivity, correctness via strict typing, and speed comparable to Node.js / Go thanks to asynchronous support.

## 2. Why FastAPI?
FastAPI is chosen for this project because it provides:
- Automatic interactive API documentation (Swagger UI and ReDoc) without extra configuration.
- Built-in request validation and serialization using Python type hints.
- First-class async support for efficient I/O (useful for future DB calls, external APIs).
- Dependency Injection system for clean separation of concerns (auth, DB sessions, etc.).
- Excellent developer experience (editor autocompletion, fewer runtime errors).

## 3. Core Concepts (FastAPI in a Nutshell)
- Application instance: `app = FastAPI(title="Spend Wise Server")`
- Path operations: Decorators like `@app.get("/")`, `@app.post("/items")` define endpoints.
- Request body & params: Declared via function parameters and Pydantic models.
- Response: Return Python dicts, lists, Pydantic models; FastAPI auto-converts to JSON.
- Automatic docs: Available at `/docs` (Swagger UI) and `/redoc`.
- Testing: Use `fastapi.testclient.TestClient` (built on `requests`) for simple sync tests.
- Running: Use an ASGI server such as Uvicorn: `uvicorn app.main:app --reload`.

## 4. How FastAPI Is Used in This Project
Current implementation (see `app/main.py`):
- Creates a FastAPI app with a custom `title` that appears in the auto-generated docs.
- Defines a root GET endpoint `/` returning a JSON health message.
- Tested via `tests/test_main.py` using `TestClient` to verify status code and response body.

Example excerpt from the existing code:
```python
from fastapi import FastAPI

app = FastAPI(title="Spend Wise Server")

@app.get("/", summary="Scratch root endpoint")
def read_root():
    return {"message": "Spend Wise server is alive"}
```

### Project Files Involved
- `app/main.py`: FastAPI app instance + endpoints.
- `tests/test_main.py`: Pytest-based tests using FastAPI's test client.
- `requirements.txt`: Lists FastAPI, Uvicorn, pytest, httpx (httpx can support async tests / external calls later).

## 5. Running the API Locally
```bash
 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start server (auto-reload for dev)
uvicorn app.main:app --reload --port 8000
```
Access:
- Root endpoint: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 6. Adding New Endpoints (Example)
Suppose you want a ping endpoint and a plain text endpoint mentioned in the README.
```python
from fastapi.responses import PlainTextResponse

@app.get("/ping", summary="Basic health ping")
async def ping():
    return {"pong": True}

@app.get("/text", response_class=PlainTextResponse, summary="Plain text health")
def text():
    return "Spend Wise server is alive"
```
Notes:
- `async def` enables concurrency for I/O-bound operations.
- `response_class=PlainTextResponse` instructs FastAPI to return plain text rather than JSON.

## 7. Request & Response Modeling (Future)
For more complex endpoints (e.g., expenses, users), define Pydantic models:
```python
from pydantic import BaseModel

class ExpenseIn(BaseModel):
    description: str
    amount: float
    category: str | None = None

class ExpenseOut(ExpenseIn):
    id: int
```
Then use them in endpoints:
```python
@app.post("/expenses", response_model=ExpenseOut)
async def create_expense(expense: ExpenseIn):
    # persist (placeholder)
    return ExpenseOut(id=1, **expense.model_dump())
```
Benefits:
- Automatic input validation (e.g., type mismatches raise 422 errors).
- Clean, documented schemas in `/docs`.

## 8. Error Handling & Validation
FastAPI auto-generates 422 responses for validation errors. Custom exceptions can be added:
```python
from fastapi import HTTPException

@app.get("/secure")
async def secure_endpoint():
    raise HTTPException(status_code=401, detail="Not authenticated")
```
Global handlers and middleware can be added for logging, CORS, auth, etc.

## 9. Testing Strategy
Current tests use synchronous `TestClient`:
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Spend Wise server is alive"}
```