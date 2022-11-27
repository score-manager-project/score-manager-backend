from app.auth.deps import get_profile
from app.models.responses import ProfileResponse
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
async def read_profile(profile: ProfileResponse = Depends(get_profile)):
    return profile
