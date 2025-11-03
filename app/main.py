from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime, timezone

app = FastAPI(title="Spend Wise Server")

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
