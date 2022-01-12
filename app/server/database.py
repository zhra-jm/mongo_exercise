from datetime import datetime

from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoSingleton:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(*args, **kwargs)
        return cls.instance

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['academy_denormalized']

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


class MongoStorage:

    def __init__(self):
        self.mongo = MongoSingleton()

    def store_many(self, data, collection, *args):
        collection = getattr(self.mongo.db, collection)
        collection.insert_many(data)

    def store_one(self, data, collection, *args):
        collection = getattr(self.mongo.db, collection)
        collection.insert_one(data)

    def load(self, collection_name, filter_name=None):
        collection = self.mongo.db[collection_name]
        if filter_name is not None:
            data = collection.find(filter_name)
        else:
            data = collection.find()
        return data

    def update(self, obj_id):
        self.mongo.db.classes.find_one_and_update(
            {"_id": ObjectId(obj_id)},
            {"$set": {"end_date": datetime.now()}}
        )

    def delete(self, obj_id):
        self.mongo.db.students.delete_one({'_id': ObjectId(obj_id)})
