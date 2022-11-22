import httpx
from app.core.config import settings
from app.models.responses import ProfileResponse, TokenResponse

from .common import BASE_URL


async def get_token(code: str) -> TokenResponse:
    """Fetch token from NYCU OAuth server."""

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.post(
            "/o/token/",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": settings.NYCU_OAUTH_CLIENT_ID,
                "client_secret": settings.NYCU_OAUTH_CLIENT_SECRET,
                "redirect_uri": settings.NYCU_OAUTH_REDIRECT_URI,
            },
        )

    return response.json()


async def get_profile(token: str) -> ProfileResponse:
    """Use the token to get the profile of current user."""

    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get(
            "/api/profile/",
            headers={"Authorization": f"Bearer {token}"},
        )

    print(f"{response=}")
    print(f"{response.json()=}")

    if not response.is_success:
        return None

    return response.json()
