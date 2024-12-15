import collections
from django.conf import settings
from .dbconnector import MongoMobileApp
from rest_framework.decorators import api_view
from .jsonutility import JSONEncoder
import json
from rest_framework.response import Response
from bson import ObjectId
from bson.objectid import ObjectId

def systemCheck():
    collections = MongoMobileApp.listCollections()
    if 'events' not in collections:
        MongoMobileApp.createCollection('events') 
    if 'resources' not in collections:
        MongoMobileApp.createCollection('resources')
    if 'participants' not in collections:
        MongoMobileApp.createCollection('participants')
    return True

class formModel:
    def todb(params):
        result = {}
        if '_id' in params:
            result['_id'] = ObjectId(params['_id'])
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'eventDescription' in params:
            result['eventDescription'] = params['eventDescription']
        else:
            result['eventDescription'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = "active"
        else:
            result['status'] = "inActive"
        return result

    def fromdb(params):
        result = {}
        if '_id' in params:
            result['_id'] = str(params['_id'])
        else:
            result['payloadId'] = ''
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'eventDescription' in params:
            result['eventDescription'] = params['eventDescription']
        else:
            result['eventDescription'] = ""
        if 'images' in params:
            if 'coverPhoto' in params['images']:
                result['images'] = params['images']['coverPhoto'][0]['img']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = "inActive"
        return result

class payloadModel:
    def todb(params):
        result = {}
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'eventDescription' in params:
            result['eventDescription'] = params['eventDescription']
        else:
            result['eventDescription'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = "active"
        else:
            result['status'] = "inActive"
        return result

    def fromdb(params):
        result = {}
        if '_id' in params:
            result['_id'] = str(params['_id'])
        else:
            result['payloadId'] = ''
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'eventDescription' in params:
            result['eventDescription'] = params['eventDescription']
        else:
            result['eventDescription'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = "inActive"
        return result

@api_view(['GET'])
def getEvents(request):
    filter = {}
    filter['status'] = "active"
    records = MongoMobileApp.find('events', filter)
    i = 0
    while i<len(records):
        records[i] = formModel.fromdb(records[i])
        i = i+1
    return Response(records)

@api_view(['GET'])
def getEvent(request):
    params = request.query_params
    filter = {}
    if 'payloadId' in params:
        filter['_id'] = ObjectId(params['payloadId'])
    record = MongoMobileApp.find('events', filter)
    i = 0
    while i<len(record):
        record[i] = payloadModel.fromdb(record[i])
        i = i+1
    return Response(record)

@api_view(['POST'])
def createEvent(request):
    systemCheck()
    body = json.loads(request.body.decode('utf-8'))
    body = formModel.todb(body)
    records = MongoMobileApp.createOne('events',body)
    records = formModel.fromdb(body)
    return Response(records)

@api_view(['POST'])
def saveEvent(request):
    systemCheck()
    body = json.loads(request.body.decode('utf-8'))
    body = formModel.todb(body)
    print(body['_id'])
    filter = {}
    filter['_id'] = body['_id']
    records = MongoMobileApp.updateMany('events',filter,{'$set':body})
    records = formModel.fromdb(body)
    return Response("records")

@api_view(['DELETE'])
def deleteEvent(request):
    params = request.query_params
    filter = {}
    if 'payloadId' in params:
        filter['_id'] = ObjectId(params['payloadId'])
    MongoMobileApp.deleteMany('events', filter)
    return Response("Deleted")


# Custom JSON serializer for MongoDB's ObjectId
def json_converter(o):
    if isinstance(o, ObjectId):
        return str(o)  # Convert ObjectId to string
    raise TypeError(f"Type {o} not serializable")