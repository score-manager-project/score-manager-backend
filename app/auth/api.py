from __future__ import annotations

from app.models.responses import TokenResponse
from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse

from . import utils

router = APIRouter()


@router.get(
    "/login",
    response_description="Redirect to NYCU OAuth authorization page",
)
async def get_authorization_code():
    return RedirectResponse(
        url=utils.get_authorization_url(),
        status_code=status.HTTP_302_FOUND,
    )


@router.get("/token", response_model=TokenResponse)
async def get_token(code: str):
    return await utils.fetch_token(code)
