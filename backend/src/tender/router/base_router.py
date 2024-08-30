import logging

from fastapi import APIRouter


class BaseRouter:
    def __init__(self, logger: logging.Logger, prefix: str, tags: list[str], responses: dict | None = None):
        self.logger = logger
        self.router = APIRouter(
            prefix=prefix,
            tags=tags,
            responses={404: {"description": "Not found"}} if not responses else responses,
        )
