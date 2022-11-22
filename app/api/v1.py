from fastapi import APIRouter

from .routes import profile

router = APIRouter()

router.include_router(profile.router, prefix="/profile", tags=["profile"])
