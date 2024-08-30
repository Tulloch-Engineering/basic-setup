import json
import logging
import os

from src.constants.enum import ErrorResponse
from tullochdb import db

logger = logging.getLogger(__name__)


class DatabaseUtil:

    def get_db_tool(self):
        """
        Utility function uses tullochdb internal tool to setup the db_tool.

        :param None

        :yield started database tool from parameters from .env.
        :raises Exception: Any generic error that is raised.
        :finally closes database object.
        """
        try:
            db_tool = db.TullochDatabaseTool()
            db_tool.startup(connection_string=os.environ.get("AZURE_SQL_CONNECTIONSTRING"))
            logger.info(f"Connection to Database Successful! {db_tool}")
            yield db_tool
        except Exception:
            logger.error(ErrorResponse.DATABASE_KEY.value)
        finally:
            db_tool.close()

    def db_format_json(self, value: json) -> json:
        return json.loads(value) if value else None
