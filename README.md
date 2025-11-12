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
## &
### 2. Install dependencies
```bash
./run setup
```
### 3. Run the development server
```bash
./run server
```
Visit: http://127.0.0.1:8000

Interactive API docs (Swagger UI): http://127.0.0.1:8000/docs
ReDoc docs: http://127.0.0.1:8000/redoc

### 4. Run tests
```bash
./run test
```

### 5. Run linting and auto-fix issues
```bash
./run lint
```

This command will:
- Format your code using `ruff format`
- Fix linting issues automatically using `ruff check --fix`

## Code Quality

### Linting & Formatting
This project uses **Ruff** for linting and formatting. Ruff is a fast, modern Python linter written in Rust that combines the functionality of multiple tools (black, flake8, isort, etc.) into one.

**Why Ruff?**
- ⚡ **10-100x faster** than traditional tools
- 🔧 **All-in-one** - replaces black, flake8, isort, and more
- 🛠️ **Auto-fix capability** - automatically fixes many issues
- 📦 **Single dependency** - simpler than managing multiple tools

See [docs/LINTING_COMPARISON.md](docs/LINTING_COMPARISON.md) for a detailed comparison of linting tools.

**Configuration:** Linting rules are configured in `pyproject.toml`

## Git Hooks

Git hooks are automatically set up when you run `./run setup`. This will install the pre-commit hook to your local `.git/hooks` directory. A pre-commit hook is configured to automatically run **linting checks** and **unit tests** before each commit. This ensures that no broken or improperly formatted code gets committed to the repository.

**How it works:**
1. **Linting checks** (runs first):
   - Checks code formatting with `ruff format --check`
   - Checks code quality with `ruff check`
   - If formatting or linting fails, commit is aborted
2. **Unit tests** (runs after linting passes):
   - Executes `pytest` on the `tests/` directory
   - If tests fail, commit is aborted

**If checks fail:**
- Run `./run lint` to auto-fix formatting and linting issues
- Fix any failing tests
- Try committing again

**To bypass the hook (not recommended):**
```bash
git commit --no-verify
```

**Note:** The hook automatically detects and activates virtual environments (`.venv` or `venv`) if they exist.

## Example Responses
`GET /` -> `{ "message": "Spend Wise server is alive" }`

`GET /ping` -> `{ "pong": true }`

`GET /text` -> `Spend Wise server is alive`

## Next Steps
- Add models for users, groups, expenses
- Integrate database (e.g., PostgreSQL with SQLModel or SQLAlchemy)
- Authentication & authorization (JWT)
- CI setup (GitHub Actions)
