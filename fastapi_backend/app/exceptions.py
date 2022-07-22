from fastapi import HTTPException, status

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)

empty_access_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Access token is null.",
    headers={"WWW-Authenticate": "Bearer"},
)

invalid_login_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password.",
    headers={"WWW-Authenticate": "Bearer"},
)

user_not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User not found.",
    headers={"WWW-Authenticate": "Bearer"},
)

expired_access_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Access token has expired.",
    headers={"WWW-Authenticate": "Bearer"},
)

refresh_token_not_found_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Refresh token not found.",
)

invalid_refresh_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token."
)
registration_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Username is already registered."
)

project_create_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Unable to created project.",
)
