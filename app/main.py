from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Spend Wise Server")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow only localhost:5173 for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Capture application start time (UTC, timezone-aware) for uptime calculations
START_TIME = datetime.now(timezone.utc)


@app.get("/", summary="Scratch root endpoint")
def read_root():
    return {"message": "Spend Wise server is alive"}


# Health check endpoint returning status and uptime
@app.get("/health", summary="Health check endpoint")
def health():
    now = datetime.now(timezone.utc)
    uptime_seconds = (now - START_TIME).total_seconds()
    return {
        "status": "ok",
        "uptime_seconds": uptime_seconds,
    }
