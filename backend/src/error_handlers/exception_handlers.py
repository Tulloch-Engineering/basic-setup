import logging

from fastapi import HTTPException, Request
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.exc import SQLAlchemyError
from src.constants.enum import ErrorResponse


class ExceptionHandlers:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.error = self.__Error(self.logger)

    async def file_not_found_handler(self, request: Request, exc: FileNotFoundError):
        self.error.unknown_file(exc)

    async def response_validation_exception_handler(self, request: Request, exc: ResponseValidationError):
        self.error.validation(exc)

    async def value_exception_handler(self, request: Request, exc: ValueError):
        self.error.value(exc)

    async def permission_handler(self, request: Request, exc: PermissionError):
        self.error.permission(exc)

    async def sqlalchemy_exception_handler(self, request: Request, exc: SQLAlchemyError):
        self.error.database(exc)

    async def exception_handler(self, request: Request, exc: Exception):
        self.error.unknown(exc)

    class __Error:
        def __init__(self, logger: logging.Logger):
            self.logger = logger

        def __handler(self, e, status_code: int, error_response: ErrorResponse):
            self.logger.error(f"e: {e} | status_code: {status_code} | error_response: {error_response}")
            raise HTTPException(status_code=status_code, detail=error_response.value)

        def validation(self, e: str, status_code: int = 400, error_msg: ErrorResponse = ErrorResponse.VALIDATION):
            self.__handler(e, status_code, error_msg)

        def value(self, e: str, status_code: int = 400, error_msg: ErrorResponse = ErrorResponse.VALUE):
            self.__handler(e, status_code, error_msg)

        def database(self, e: str, status_code: int = 400, error_msg: ErrorResponse = ErrorResponse.DATABASE):
            self.__handler(e, status_code, error_msg)

        def incorrect_file(self, e: str, status_code: int = 400, error_msg: ErrorResponse = ErrorResponse.INVALID_FILE):
            self.__handler(e, status_code, error_msg)

        def permission(self, e: str, status_code: int = 403, error_msg: ErrorResponse = ErrorResponse.PERMISSION):
            self.__handler(e, status_code, error_msg)

        def unknown_file(self, e: str, status_code: int = 404, error_msg: ErrorResponse = ErrorResponse.FILE):
            self.__handler(e, status_code, error_msg)

        def unknown(self, e: str, status_code: int = 500, error_msg: ErrorResponse = ErrorResponse.UNKNOWN):
            self.__handler(e, status_code, error_msg)
