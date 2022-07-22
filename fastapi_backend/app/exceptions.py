from fastapi import HTTPException, status

registration_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="Username is already registered."
)