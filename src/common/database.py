import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert_method(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find_method(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_method(collection, query, data):
        # upsert = if there is no entry in database, do an INSERT
        Database.DATABASE[collection].update(query, data, upsert=True)