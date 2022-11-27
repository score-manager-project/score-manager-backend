from fastapi import HTTPException, status


class CredentialError(HTTPException):
    """Raised when error occurred in authorization steps."""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not validate credentials",
        )
