# spend-wise-server

FastAPI server for the Spend Wise application.

## Features
- Root endpoint returning JSON alive message
- Ping endpoint for basic health check
- Plain text scratch endpoint

## Project Structure
```
app/
  main.py                 # FastAPI app factory and primary endpoints
  core/
    config.py             # Pydantic BaseSettings for env-driven config
    security.py           # Placeholder security helpers (JWT token stub)
    logging_config.py     # Central logging setup function
  api/
    deps.py               # Dependency functions (e.g., get_settings)
    v1/
      router.py           # APIRouter for version 1 endpoints
      endpoints/          # (future) individual endpoint modules
  models/                 # (future) ORM / domain models
  schemas/                # (future) Pydantic schemas
  services/               # (future) business logic layer
  db/                     # (future) database session utilities
  utils/                  # (future) helper utilities
requirements.txt          # Python dependencies
tests/
  test_main.py            # Pytest tests for root endpoint
```

## Getting Started
### 1. Create and activate a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the development server
```bash
uvicorn app.main:app --reload --port 8000
```
Visit: http://127.0.0.1:8000

Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs
ReDoc docs: http://127.0.0.1:8000/redoc

### 4. Run tests
```bash
pytest -q
```

## Example Responses
`GET /` -> `{ "message": "Spend Wise server is alive" }`

`GET /ping` -> `{ "pong": true }`

`GET /text` -> `Spend Wise server is alive`

## Next Steps
- Add models for users, groups, expenses
- Integrate database (e.g., PostgreSQL with SQLModel or SQLAlchemy)
- Authentication & authorization (JWT)
- CI setup (GitHub Actions)
