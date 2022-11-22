from app import app


@app.get("/")
async def read_root():
    return {"ping": "pong"}
