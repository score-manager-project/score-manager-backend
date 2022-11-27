import httpx
from app.core.config import settings
from app.models.responses import TokenResponse

from .constants import NYCU_OAUTH_URL


def get_authorization_url() -> str:
    """Return the NYCU OAuth authorization URL with query parameters."""

    return (
        f"{NYCU_OAUTH_URL}/authorize/"
        f"?client_id={settings.NYCU_OAUTH_CLIENT_ID}&response_type=code"
        f"&scope=profile&redirect_uri={settings.NYCU_OAUTH_REDIRECT_URI}"
    )


async def fetch_token(code: str) -> TokenResponse:
    """Fetch token from NYCU OAuth server."""

    async with httpx.AsyncClient(base_url=NYCU_OAUTH_URL) as client:
        response = await client.post(
            "/token/",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": settings.NYCU_OAUTH_CLIENT_ID,
                "client_secret": settings.NYCU_OAUTH_CLIENT_SECRET,
                "redirect_uri": settings.NYCU_OAUTH_REDIRECT_URI,
            },
        )

    return response.json()
