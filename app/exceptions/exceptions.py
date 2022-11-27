from fastapi import HTTPException


class CustomHTTPException(HTTPException):
    status_code: int

    def __init__(self):
        super().__init__(status_code=self.status_code)


class NotFoundError(CustomHTTPException):
    status_code = 404
