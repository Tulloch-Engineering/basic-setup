import logging
import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from src.constants.enum import ErrorResponse
from src.error_handlers.exception_handlers import ExceptionHandlers
from src.tender.router.database_test import DatabaseRouter
from src.util.db_util import DatabaseUtil
from starlette.responses import RedirectResponse
from tullochdb import db

current_directory = dirname(abspath(__file__))
load_dotenv(join(current_directory, ".env"))


class BackendAppService:

    def __init__(self):
        logger = logging.getLogger(__name__)
        exception_handlers = ExceptionHandlers(logger)

        self.app = FastAPI(title=os.environ.get("APP_NAME"), version=os.environ.get("VERSION"))

        self.app.add_middleware(
            CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True
        )

        # Redirect / -> Swagger-UI documentation
        @self.app.get("/")
        def redirect_endpoint():
            """
            # Redirect
            to documentation (`/docs/`).
            """
            return RedirectResponse(url="/docs/")

        try:
            db_tool: db.TullochDatabaseTool = next(DatabaseUtil().get_db_tool())

            database_router = DatabaseRouter(logger, db_tool).router

            self.app.include_router(database_router)

            self.app.add_exception_handler(
                ResponseValidationError, exception_handlers.response_validation_exception_handler
            )
            self.app.add_exception_handler(ValueError, exception_handlers.value_exception_handler)
            self.app.add_exception_handler(SQLAlchemyError, exception_handlers.sqlalchemy_exception_handler)
            self.app.add_exception_handler(Exception, exception_handlers.exception_handler)
            self.app.add_exception_handler(FileNotFoundError, exception_handlers.file_not_found_handler)

        except StopIteration:
            logger.info(ErrorResponse.DATABASE.value)


app = BackendAppService().app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, debug=True, host="0.0.0.0", port=8080)
