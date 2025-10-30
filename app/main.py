from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="Spend Wise Server")

@app.get("/", summary="Scratch root endpoint")
def read_root():
    return {"message": "Spend Wise server is alive"}
