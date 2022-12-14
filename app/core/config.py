from __future__ import annotations

from pydantic import BaseSettings


class DetaSettings(BaseSettings):
    """Settings for Deta Base."""

    DETA_PROJECT_KEY: str


class NYCUAuthSettings(BaseSettings):
    """Settings for NYCU OAuth."""

    NYCU_OAUTH_CLIENT_ID: str
    NYCU_OAUTH_CLIENT_SECRET: str
    NYCU_OAUTH_REDIRECT_URI: str


class Settings(DetaSettings, NYCUAuthSettings):
    """Overall settings for application"""

    class Config:
        env_file = ".env"


settings = Settings()
