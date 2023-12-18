import copy

from scripts.constants.app_configuration import *
from scripts.logging.log_module import logger as log
from scripts.utils.MongoUtility import MongoUtility
import json


class MongoData:
    def __init__(self):
        try:
            self.mongo_obj = MongoUtility(mongodb_host, mongodb_port)

        except Exception as e:
            log.error(f"Exception Occurred Due to {e}")

    def display(self):

        final_json = {"status": "failed"}
        try:
            mongo_device_data = self.mongo_obj.fetch_all(mongo_database, mongoDB_crud)
            for each_data in mongo_device_data:
                print(each_data)
                final_json["status"] = 'success'
                final_json['data'] = each_data['name']
        except Exception as e:
            log.error("Exception occurred while fetching data" + str(e))
            final_json["message"] = "Exception occurred while displaying the data"
        return final_json

    def update(self, json_object):
        final_json = {"status": "Failed"}
        try:
            json_data = copy.deepcopy(json_object)
            json_data = json.loads(json_data.json())

            if "action" in json_data and json_object.action.lower() == "add":

                json_format = dict()

                """
                Things to be added
                """
                self.mongo_obj.database_insertion(mongo_database, mongoDB_crud, json_format)
                final_json["status"] = True
                final_json["message"] = "Added successfully "

            elif "action" in json_data and json_object.action.lower() == "update":
                condition = {"name": "Value"}
                " condition is used to fetch particular record from db "
                json_format = dict()

                """
                Things to be updated
                """
                self.mongo_obj.update_one(mongo_database, mongoDB_crud, condition, json_format)
                final_json["status"] = True
                final_json["message"] = "Updated successfully"

            elif "action" in json_data and json_object.action.lower() == "delete":
                condition = {"name": "value"}
                self.mongo_obj.record_bulk_remove(mongo_database, mongoDB_crud, condition)
                final_json["status"] = True

                final_json["message"] = "Deleted successfully "
        except Exception as e:
            log.info("Exception occurred while saving the data " + str(e))
        return final_json
