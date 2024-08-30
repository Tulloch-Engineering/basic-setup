import logging

from src.tender.router.base_router import BaseRouter
from tullochdb import db


class DatabaseRouter(BaseRouter):

    def __init__(self, logger: logging.Logger, db_tool: db.TullochDatabaseTool):
        super().__init__(logger=logger, prefix="/database/v1", tags=["Database"])

        @self.router.get("/", response_model=list, status_code=200)
        async def select_one():
            """
            Tests the database by running SELECT 1

            :param None.

            :return the execute_query function of the sql.
            """
            return db_tool.execute_query("SELECT 1")
