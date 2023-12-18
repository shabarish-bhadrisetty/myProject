import configparser

__config = configparser.ConfigParser()
__config.read("conf/application.conf")

# LOG HANDLERS

LOG_BASE_PATH = __config.get('LOG', 'base_path')
LOG_LEVEL = __config.get('LOG', 'level')
FILE_BACKUP_COUNT = __config.get('LOG', 'file_backup_count')
FILE_BACKUP_SIZE = __config.get('LOG', 'file_size_mb')
FILE_NAME = LOG_BASE_PATH + __config.get('LOG', 'file_name')
LOG_HANDLERS = __config.get('LOG', 'handlers')

# Server Details
PORT = __config.get('SERVER', 'port')
HOST = __config.get('SERVER', 'host')


mongodb_host = __config.get("mongodb", "host")
mongodb_port = int(__config.get("mongodb", "port"))
mongo_database = __config.get("mongodb", "db_test")
mongoDB_crud = __config.get("mongodb","db_collection")

sqldb_host = __config.get('sqldb', 'host')
sql_port = int(__config.get('sqldb', 'port'))
table_name = __config.get('sqldb','table_name')
sql_db_name = __config.get('sqldb','db_name')
sql_password = __config.get('sqldb','password')
sql_username = __config.get('sqldb','user_name')



