import json

from pymongo import MongoClient
from scripts.logging.log_module import logger


class MongoUtility(object):
    def __init__(self, mongo_host, mongo_port):
        try:
            self.connection = MongoClient(mongo_host, mongo_port)
        except Exception as e:
            print(e)

    def database_insertion(self, db_name, collection_name, query_json):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            mg_response = docid.insert(query_json, check_keys=False)
        except Exception as e:
            logger.error("Exception while inserting the data" + str(e))
        return mg_response

    def database_insertion_insert_many(self, db_name, collection_name, query_json):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            mg_response = docid.insert_many(query_json)
        except Exception as e:
            logger.error("Exception while insertion of many data" + str(e))
        return mg_response

    def search_record_by_query(self, db_name, collection_name, query_json):
        mg_response = {}
        try:
            response = {}
            docid = self.connection[db_name][collection_name]
            for key, value in query_json.items():
                response = docid.find({key: value})
            mg_response = self.fetch_records_from_object(response)
        except Exception as e:
            logger.error("Exception while searching the record" + str(e))
        return mg_response

    def fetch_all(self, db_name, collection_name):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            response = docid.find()
            mg_response = self.fetch_records_from_object(response)
        except Exception as e:
            logger.error("Exception while fetching the data" + str(e))
        return mg_response

    def record_bulk_remove(self, db_name, collection_name, query_json):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            for key, value in query_json.items():
                mg_response = json.dumps(docid.remove({key: value}, multi=True))
        except Exception as e:
            logger.error("Exception while removing the record" + str(e))
        return mg_response

    def record_remove_by_id(self, db_name, collection_name, record_id):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            mg_response = docid.delete_one({"_id": ObjectId(record_id)})

        except Exception as e:
            logger.error("Exception while removing the record by id" + str(e))
        return mg_response

    def fetch_record_by_id(self, db_name, collection_name, record_id, object_check=None):
        mg_response = {}
        try:
            doc_id = self.connection[db_name][collection_name]
            if object_check:
                response = doc_id.find({"_id": ObjectId(record_id)})
            else:
                response = doc_id.find({"_id": record_id})
            mg_response = self.fetch_records_from_object(response)
        except Exception as e:
            logger.error("Exception while fetching the record by id" + str(e))
        return mg_response

    @staticmethod
    def fetch_records_from_object(body):
        final_list = []
        try:
            for doc in body:
                final_json = doc
                final_list.append(final_json)
            return final_list
        except Exception as e:
            logger.error("Exception while fetching the records from object" + str(e))

    def new_feild_update_by_id(self, db_name, collection_name, update_json):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            for key, value in update_json.items():
                mg_response = docid.update({"_id": update_json["_id"]}, {"$set": {key: value}})
        except Exception as e:
            logger.exception("Exception while updating the new_field by id" + str(e))
        return mg_response

    def sort_records(self, db_name, collection_name, key, direction=1):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            mg_response = docid.find().sort({key: direction})
        except Exception as e:
            logger.error("Exception while sorting the records" + str(e))
        return mg_response

    def update_one(self, db_name, collection_name, query_json, update_json):
        mg_response = {}
        try:
            docid = self.connection[db_name][collection_name]
            for key, value in update_json.items():
                mg_response = docid.update({'$and': [query_json]},
                                           {"$set": {key: value}})
        except Exception as e:
            logger.error("Exception while updating the one collection" + str(e))
            print(e)
        return mg_response
