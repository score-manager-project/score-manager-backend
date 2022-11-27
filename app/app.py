from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import auth
from .api import v1

app = FastAPI(title="Scoreboard Manager API Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"ping": "pong"}


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(v1.router, prefix="/api/v1")
