#!/usr/bin/env python
import json
import pymongo

from django.conf import settings
class MongoMobileApp:
    __instance = None
    __mongoConfig = {}
    __collections = []
    def __init__(self):
        self.logger = logging.getLogger("Mongo Connection")
        if self.__instance == None:
            self.__mongoConfig = settings.MONGOMOBILEAPP 
            if self.__mongoConfig['authentication'] == 'True' or self.__mongoConfig['authentication'] == 'true' or self.__mongoConfig['authentication'] == True:
                baseString = "mongodb+srv://"+ self.__mongoConfig['username']+ ":"+ self.__mongoConfig['password']+"@cluster0.xebhn.mongodb.net/"
                connectionString = baseString
                client = pymongo.MongoClient(connectionString)
            else:
                baseString = "mongodb://"+ self.__mongoConfig['host']+":"+ str(self.__mongoConfig['port'])+"/"+ self.__mongoConfig['dbname']+"?authSource=admin&tls=true"
                connectionString = baseString
                client = pymongo.MongoClient(connectionString)
            self.__instance = client[self.__mongoConfig['dbname']] 
            self.__collections = self.__instance.list_collection_names();  
        pass
    @staticmethod
    def getInstance():
        if MongoMobileApp.__instance == None:
            MongoMobileApp.__mongoConfig = settings.MONGOMOBILEAPP
            if MongoMobileApp.__mongoConfig['authentication'] == True or MongoMobileApp.__mongoConfig['authentication'] == 'True' or MongoMobileApp.__mongoConfig['authentication'] == 'true':
                baseString = "mongodb+srv://"+ MongoMobileApp.__mongoConfig['username']+ ":"+ MongoMobileApp.__mongoConfig['password']+"@cluster0.xebhn.mongodb.net/"
                connectionString = baseString
                client = pymongo.MongoClient(connectionString)
            else:
                baseString = "mongodb://"+ MongoMobileApp.__mongoConfig['host']+":"+ str(MongoMobileApp.__mongoConfig['port'])+"/"+ MongoMobileApp.__mongoConfig['dbname']+"?authSource=admin"
                connectionString = baseString
                client = pymongo.MongoClient(connectionString)
            MongoMobileApp.__instance = client[MongoMobileApp.__mongoConfig['dbname']]
            MongoMobileApp.__collections = MongoMobileApp.__instance.list_collection_names()
        return MongoMobileApp.__instance
    def listCollections():
        MongoMobileApp.getInstance()
        return MongoMobileApp.__collections
    def createCollection(collectionName, schema={}):
        db = MongoMobileApp.getInstance()
        try:
            if collectionName not in db.list_collection_names():  # Check if collection exists
                # Create collection with validation schema if provided
                if schema:
                    db.create_collection(collectionName, validator=schema)
                else:
                    db.create_collection(collectionName)  # Create without schema validation
                print(f"Collection '{collectionName}' created successfully.")
                return True
            else:
                print(f"Collection '{collectionName}' already exists.")
                return False
        except pymongo.errors.PyMongoError as e:
            print(f"Error creating collection: {e}")
            return False
    def findOne(collection):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        return dbcollection.find_one("")
    def findAll(collection):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        data = []
        for record in dbcollection.find(""):
            data.append(record)
        return data
    def find(collection, query = None):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        data = []
        if query == None:
            for record in dbcollection.find(""):
                data.append(record)
        else:
            for record in dbcollection.find(query):
                data.append(record)            
        return data
    def createOne(collection, data):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        if type(data) == list:
            for item in data:
                if type(item) == dict:
                    result = dbcollection.insert_one(item)
                    return result.inserted_id
        elif type(data) == dict:
            result = dbcollection.insert_one(data)
            return result.inserted_id
        else:
            return None
    def updateOne(collection, query, newvalues):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.update_one(query, newvalues)
        return result.modified_count
    def updateMany(collection, query, newvalues):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.update_many(query, newvalues)
        return result.modified_count
    def deleteOne(collection, query):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.delete_one(query)
        return result.deleted_count
    def deleteMany(collection, query):
        print(collection)
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.delete_many(query)
        return result.deleted_count
    def listCollections():
        db = MongoMobileApp.getInstance()
        return db.list_collection_names()
