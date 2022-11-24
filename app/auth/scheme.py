from fastapi.security.oauth2 import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer

nycu_oauth_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/auth/login",
    tokenUrl="/auth/token",
    scopes={"profile": "Get User Profile"},
    description="NYCU OAuth",
)
