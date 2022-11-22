from __future__ import annotations

from typing import Optional

from app.core.config import settings
from app.models.responses import TokenResponse
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from .common import BASE_URL
from .utils import get_token

router = APIRouter()


@router.get("/login", response_model=TokenResponse)
async def login(code: Optional[str] = None):
    if code is None:
        return RedirectResponse(
            f"{BASE_URL}/o/authorize/"
            f"?client_id={settings.NYCU_OAUTH_CLIENT_ID}"
            "&response_type=code"
            "&scope=profile"
            f"&redirect_uri={settings.NYCU_OAUTH_REDIRECT_URI}"
        )

    token_response = await get_token(code)
    return token_response
