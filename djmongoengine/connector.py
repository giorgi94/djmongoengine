import pymongo
from django.conf import settings


class MongoConnector:
    def __init__(self, alias="default"):
        MONGODB_DATABASES = settings.MONGODB_DATABASES
        CONFIG = MONGODB_DATABASES[alias]

        dbname = CONFIG["name"]
        username = CONFIG.get("username")
        password = CONFIG.get("password")

        credentials = ""

        if username and password:
            credentials = f"{username}:{password}@"

        uri = "mongodb://{credentials}{host}:{port}".format(
            credentials=credentials, **CONFIG
        )

        self.client = pymongo.MongoClient(uri)
        self.db = self.client[dbname]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self, **kwargs):
        self.client.close()

    def update_one(self, selector, collection, data):
        self.db[collection].update_one(selector, {"$set": data}, upsert=True)

    def create_index(self, collection, name):
        return self.db[collection].create_index([(name, 1)])

    def info_index(self, collection):
        return self.db[collection].index_information()
