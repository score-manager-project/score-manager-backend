import httpx
from app.models.responses import ProfileResponse
from fastapi import Depends

from . import nycu_oauth_scheme
from .constants import NYCU_API_URL
from .error import CredentialError


async def get_profile(token: str = Depends(nycu_oauth_scheme)) -> ProfileResponse:
    """Use the token to get the profile of current user."""

    async with httpx.AsyncClient(base_url=NYCU_API_URL) as client:
        response = await client.get(
            "/profile/",
            headers={"Authorization": f"Bearer {token}"},
        )

    if not response.is_success:
        raise CredentialError()

    return response.json()
