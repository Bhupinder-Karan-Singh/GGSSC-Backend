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
            #client = pymongo.MongoClient("mongodb://ranDBAdmin:testserver81@172.25.220.81/ranDB?authSource=admin")
            if self.__mongoConfig['authentication'] == 'True' or self.__mongoConfig['authentication'] == 'true' or self.__mongoConfig['authentication'] == True:
                baseString = "mongodb://"+ self.__mongoConfig['username']+ ":"+ self.__mongoConfig['password']+"@"+ self.__mongoConfig['host']+":"+ str(self.__mongoConfig['port'])+"/"+ self.__mongoConfig['dbname']+"?authSource=admin&tls=true"
                tlsString = "&tls=true&tlsCertificateKeyFile=" + self.__mongoConfig['mongoCertificatePath'] + "&tlsCAFile=" +self.__mongoConfig['mongoCAPath'] + "&tlsInsecure=true"
                connectionString = baseString if self.__mongoConfig['tls'] == 'False' else baseString + tlsString
                client = pymongo.MongoClient(connectionString)
            else:
                baseString = "mongodb://"+ self.__mongoConfig['host']+":"+ str(self.__mongoConfig['port'])+"/"+ self.__mongoConfig['dbname']+"?authSource=admin&tls=true"
                tlsString = "&tls=true&tlsCertificateKeyFile=" + self.__mongoConfig['mongoCertificatePath'] + "&tlsCAFile=" +self.__mongoConfig['mongoCAPath'] + "&tlsInsecure=true"
                connectionString = baseString if self.__mongoConfig['tls'] == 'False' else baseString + tlsString
                client = pymongo.MongoClient(connectionString)
            self.__instance = client[self.__mongoConfig['dbname']] 
            self.__collections = self.__instance.list_collection_names();  
        pass
    @staticmethod
    def getInstance():
        if MongoMobileApp.__instance == None:
            MongoMobileApp.__mongoConfig = settings.MONGOMOBILEAPP
            if MongoMobileApp.__mongoConfig['authentication'] == True or MongoMobileApp.__mongoConfig['authentication'] == 'True' or MongoMobileApp.__mongoConfig['authentication'] == 'true':
                baseString = "mongodb://"+ MongoMobileApp.__mongoConfig['username']+ ":"+ MongoMobileApp.__mongoConfig['password']+"@"+ MongoMobileApp.__mongoConfig['host']+":"+ str(MongoMobileApp.__mongoConfig['port'])+"/"+ MongoMobileApp.__mongoConfig['dbname'] + "?authSource=admin"
                tlsString = "&tls=true&tlsCertificateKeyFile=" + MongoMobileApp.__mongoConfig['mongoCertificatePath'] + "&tlsCAFile=" +MongoMobileApp.__mongoConfig['mongoCAPath'] + "&tlsInsecure=true"
                connectionString = baseString if MongoMobileApp.__mongoConfig['tls'] == "False" else baseString + tlsString
                client = pymongo.MongoClient(connectionString)
            else:
                baseString = "mongodb://"+ MongoMobileApp.__mongoConfig['host']+":"+ str(MongoMobileApp.__mongoConfig['port'])+"/"+ MongoMobileApp.__mongoConfig['dbname']+"?authSource=admin"
                tlsString = "&tls=true&tlsCertificateKeyFile=" + MongoMobileApp.__mongoConfig['mongoCertificatePath'] + "&tlsCAFile=" +MongoMobileApp.__mongoConfig['mongoCAPath'] + "&tlsInsecure=true"
                connectionString = baseString if MongoMobileApp.__mongoConfig['tls'] == 'False' else baseString + tlsString
                client = pymongo.MongoClient(connectionString)
            MongoMobileApp.__instance = client[MongoMobileApp.__mongoConfig['dbname']]
            MongoMobileApp.__collections = MongoMobileApp.__instance.list_collection_names()
        return MongoMobileApp.__instance
    def listCollections():
        MongoMobileApp.getInstance()
        return MongoMobileApp.__collections
    def createCollection(collectionName, schema={}):
        try:
            MongoMobileApp.createCollection(collectionName, schema)
            return True
        except:
            return False
    def findOne(collection):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        sanitized = MongoMobileApp.sanitizeDBQuery("")
        return dbcollection.find_one(sanitized)
    def findAll(collection):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        data = []
        sanitized = MongoMobileApp.sanitizeDBQuery("")
        for record in dbcollection.find(sanitized):
            data.append(record)
        return data
    def find(collection, query = None):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        data = []
        if query == None:
            sanitized = MongoMobileApp.sanitizeDBQuery("")
            for record in dbcollection.find(sanitized):
                data.append(record)
        else:
            sanitized = MongoMobileApp.sanitizeDBQuery(query)
            for record in dbcollection.find(sanitized):
                data.append(record)            
        return data
    def createOne(collection, data):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        if type(data) == list:
            for item in data:
                if type(item) == dict:
                    result = dbcollection.insert_one(MongoMobileApp.sanitizeDBQuery(item))
                    return result.inserted_id
        elif type(data) == dict:
            result = dbcollection.insert_one(MongoMobileApp.sanitizeDBQuery(data))
            return result.inserted_id
        else:
            return None
    def updateOne(collection, query, newvalues):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.update_one(MongoMobileApp.sanitizeDBQuery(query), MongoMobileApp.sanitizeDBQuery(newvalues))
        return result.modified_count
    def updateMany(collection, query, newvalues):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.update_many(MongoMobileApp.sanitizeDBQuery(query), MongoMobileApp.sanitizeDBQuery(newvalues))
        return result.modified_count
    def deleteOne(collection, query):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.delete_one(MongoMobileApp.sanitizeDBQuery(query))
        return result.deleted_count
    def deleteMany(collection, query):
        db = MongoMobileApp.getInstance()
        dbcollection = db[collection]
        result = dbcollection.delete_many(MongoMobileApp.sanitizeDBQuery(query))
        return result.deleted_count
    def listCollections():
        db = MongoMobileApp.getInstance()
        return db.list_collection_names()
    def sanitizeDBQuery(data):
        for key in data:
            if type(data[key]) == str:
                sanitizedVal = clean(data[key])
                data[key] = sanitizedVal
        return data
