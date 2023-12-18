from scripts.logging.log_module import logger
from scripts.utils.my_sql import MysqlClient

class SqlData:

    def __init__(self):
        try:
            self.sql_obj = MysqlClient()

        except Exception as e:
            log.error(f"Exception Occurred Due to {e}")

    def fetch_data(self):
        try:
            pass
        except Exception as e:
            logger.error("Error occurred in fetch data function due to " + str(e))

    def update_data(self):
        try:
            pass
        except Exception as e:
            logger.error("Error occurred while updating data due to " + str(e))
