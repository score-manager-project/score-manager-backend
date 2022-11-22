from app.auth.utils import get_profile
from app.models.responses import ProfileResponse
from fastapi import APIRouter, Header

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
async def read_profile(token: str = Header()):
    profile = await get_profile(token)
    return profile
