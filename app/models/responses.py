from pydantic import BaseModel


class TokenResponse(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
    scope: str
    refresh_token: str


class ProfileResponse(BaseModel):
    username: str
    email: str
