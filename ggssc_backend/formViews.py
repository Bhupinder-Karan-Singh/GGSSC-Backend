import collections
from django.conf import settings
from .dbconnector import MongoMobileApp
from rest_framework.decorators import api_view
from .jsonutility import JSONEncoder
import json
from rest_framework.response import Response
from bson import ObjectId
from bson.objectid import ObjectId
import random
from django.http import HttpResponse, FileResponse, Http404, JsonResponse
from datetime import datetime
from rest_framework import status
from .validateUser import MobileUser
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
        if 'startTime' in params:
            result['startTime'] = params['startTime']
        else:
            result['startTime'] = ""
        if 'endTime' in params:
            result['endTime'] = params['endTime']
        else:
            result['endTime'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = ""
        if 'participants' in params:
            result['participants'] = params['participants']
        else:
            result['participants'] = []
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
        if 'startTime' in params:
            result['startTime'] = params['startTime']
        else:
            result['startTime'] = ""
        if 'endTime' in params:
            result['endTime'] = params['endTime']
        else:
            result['endTime'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'images' in params:
            if 'coverPhoto' in params['images']:
                result['images'] = params['images']['coverPhoto'][0]['imageFile']['img']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = ""
        if 'participants' in params:
            result['participants'] = params['participants']
        else:
            result['participants'] = []
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
        if 'startTime' in params:
            result['startTime'] = params['startTime']
        else:
            result['startTime'] = ""
        if 'endTime' in params:
            result['endTime'] = params['endTime']
        else:
            result['endTime'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = ""
        if 'participants' in params:
            result['participants'] = params['participants']
        else:
            result['participants'] = []
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
        if 'startTime' in params:
            result['startTime'] = params['startTime']
        else:
            result['startTime'] = ""
        if 'endTime' in params:
            result['endTime'] = params['endTime']
        else:
            result['endTime'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'status' in params:
            result['status'] = params['status']
        else:
            result['status'] = ""
        if 'participants' in params:
            result['participants'] = params['participants']
        else:
            result['participants'] = []
        return result

class registerModel:
    def todb(params):
        result = {}
        if 'name' in params:
            result['name'] = params['name']
        else:
            result['name'] = ""
        if 'dateOfBirth' in params:
            result['dateOfBirth'] = params['dateOfBirth']
            result['age'] = calculate_age_2(params['dateOfBirth'])
        else:
            result['dateOfBirth'] = ""
        if 'fatherName' in params:
            result['fatherName'] = params['fatherName']
        else:
            result['fatherName'] = ""
        if 'motherName' in params:
            result['motherName'] = params['motherName']
        else:
            result['motherName'] = ""
        if 'email' in params:
            result['email'] = params['email']
        else:
            result['email'] = ""
        if 'phoneNumber' in params:
            result['phoneNumber'] = params['phoneNumber']
        else:
            result['phoneNumber'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'eventId' in params:
            result['eventId'] = params['eventId']
        else:
            result['eventId'] = ""
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'isEdited' in params:
            result['isEdited'] = params['isEdited']
        else:
            result['isEdited'] = ""
        result['events'] = []
        return result

    def fromdb(params):
        result = {}
        if '_id' in params:
            result['_id'] = str(params['_id'])
        else:
            result['_id'] = ''
        if 'name' in params:
            result['name'] = params['name']
        else:
            result['name'] = ""
        if 'dob' in params:
            result['dob'] = params['dob']
        else:
            result['dob'] = ""
        if 'fatherName' in params:
            result['fatherName'] = params['fatherName']
        else:
            result['fatherName'] = ""
        if 'motherName' in params:
            result['motherName'] = params['motherName']
        else:
            result['motherName'] = ""
        if 'email' in params:
            result['email'] = params['email']
        else:
            result['email'] = ""
        if 'phoneNumber' in params:
            result['phoneNumber'] = params['phoneNumber']
        else:
            result['phoneNumber'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'eventId' in params:
            result['eventId'] = params['eventId']
        else:
            result['eventId'] = ""
        if 'eventName' in params:
            result['eventName'] = params['eventName']
        else:
            result['eventName'] = ""
        if 'location' in params:
            result['location'] = params['location']
        else:
            result['location'] = ""
        if 'events' in params:
            result['events'] = params['events']
        else:
            result['events'] = []
        if 'age' in params:
            result['age'] = params['age']
        else:
            result['age'] = ""
        return result

class candidateModel:
    def fromdb(params):
        result = {}
        if '_id' in params:
            result['_id'] = str(params['_id'])
        else:
            result['_id'] = ''
        if 'name' in params:
            result['name'] = params['name']
        else:
            result['name'] = ""
        if 'dateOfBirth' in params:
            result['dateOfBirth'] = params['dateOfBirth']
        else:
            result['dateOfBirth'] = ""
        if 'fatherName' in params:
            result['fatherName'] = params['fatherName']
        else:
            result['fatherName'] = ""
        if 'motherName' in params:
            result['motherName'] = params['motherName']
        else:
            result['motherName'] = ""
        if 'email' in params:
            result['email'] = params['email']
        else:
            result['email'] = ""
        if 'phoneNumber' in params:
            result['phoneNumber'] = params['phoneNumber']
        else:
            result['phoneNumber'] = ""
        if 'rollNumber' in params:
            result['rollNumber'] = params['rollNumber']
        else:
            result['rollNumber'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'updatedOn' in params:
            result['updatedOn'] = params['updatedOn']
        else:
            result['updatedOn'] = ""
        if 'isEdited' in params:
            result['isEdited'] = params['isEdited']
        else:
            result['isEdited'] = ""
        if 'age' in params:
            result['age'] = params['age']
        else:
            result['age'] = ""
        return result

    def todb(params):
        result = {}
        if '_id' in params:
            result['_id'] = ObjectId(params['_id'])
        if 'name' in params:
            result['name'] = params['name']
        else:
            result['name'] = ""
        if 'dateOfBirth' in params:
            result['dateOfBirth'] = params['dateOfBirth']
        else:
            result['dateOfBirth'] = ""
        if 'fatherName' in params:
            result['fatherName'] = params['fatherName']
        else:
            result['fatherName'] = ""
        if 'motherName' in params:
            result['motherName'] = params['motherName']
        else:
            result['motherName'] = ""
        if 'email' in params:
            result['email'] = params['email']
        else:
            result['email'] = ""
        if 'phoneNumber' in params:
            result['phoneNumber'] = params['phoneNumber']
        else:
            result['phoneNumber'] = ""
        if 'rollNumber' in params:
            result['rollNumber'] = params['rollNumber']
        else:
            result['rollNumber'] = ""
        if 'images' in params:
            result['images'] = params['images']
        else:
            result['images'] = ""
        if 'createdBy' in params:
            result['createdBy'] = params['createdBy']
        else:
            result['createdBy'] = ""
        if 'createdOn' in params:
            result['createdOn'] = params['createdOn']
        else:
            result['createdOn'] = ""
        if 'updatedBy' in params:
            result['updatedBy'] = params['updatedBy']
        else:
            result['updatedBy'] = ""
        if 'updatedOn' in params:
            result['updatedOn'] = params['updatedOn']
        else:
            result['updatedOn'] = ""
        if 'isEdited' in params:
            result['isEdited'] = params['isEdited']
        else:
            result['isEdited'] = ""
        if 'age' in params:
            result['age'] = calculate_age(params['dateOfBirth'])
        else:
            result['age'] = ""
        return result

@api_view(['GET'])
def getEvents(request):
    systemCheck()
    filter = {}
    filter['status'] = "Active"
    records = MongoMobileApp.find('events', filter)
    i = 0
    while i<len(records):
        records[i] = formModel.fromdb(records[i])
        i = i+1
    return Response(records)

@api_view(['GET'])
def getAllEvents(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    filter = {}
    records = MongoMobileApp.find('events', {})
    i = 0
    while i<len(records):
        records[i] = formModel.fromdb(records[i])
        i = i+1
    return Response(records)

@api_view(['GET'])
def getEvent(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

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

@api_view(['GET'])
def getCandidatesList(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    params = request.query_params
    filter = {}
    if 'payloadId' in params:
        filter['_id'] = ObjectId(params['payloadId'])
    record = MongoMobileApp.find('events', filter)
    if isinstance(record, list) and len(record)>0:
        if 'participants' in record[0] and len(record[0]['participants'])>0:
            try:
                participants = []
                for participant in record[0]['participants']:
                    filter2 = {}
                    filter2['_id'] = ObjectId(participant)
                    result = MongoMobileApp.find('participants', filter2)
                    if isinstance(result, list) and len(result)>0:
                        result = candidateModel.fromdb(result[0])
                        participants.append(result)
                    else:
                        pass
                return Response(participants)
            except:
                return Response([])
        else:
            return Response([])

@api_view(['GET'])
def getAllCandidates(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    filter = {}
    records = MongoMobileApp.find('participants', {})
    i = 0
    while i<len(records):
        records[i] = candidateModel.fromdb(records[i])
        i = i+1
    return Response(records)

@api_view(['POST'])
def createEvent(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    body = json.loads(request.body.decode('utf-8'))
    body = formModel.todb(body)
    MongoMobileApp.createOne('events',body)
    body = formModel.fromdb(body)
    return Response(body)

@api_view(['POST'])
def saveEvent(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    body = json.loads(request.body.decode('utf-8'))
    body = formModel.todb(body)
    filter = {}
    filter['_id'] = body['_id']
    record = MongoMobileApp.find('events',filter)
    if isinstance(record, list) and len(record)>0:
        body['participants'] = record[0]['participants']
        MongoMobileApp.updateMany('events',filter,{'$set':body})
        body = formModel.fromdb(body)
        return Response(body)
    else:
        return Http404

@api_view(['POST'])
def saveCandidate(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    body = json.loads(request.body.decode('utf-8'))
    body = candidateModel.todb(body)
    filter = {}
    filter['_id'] = body['_id']
    MongoMobileApp.updateMany('participants',filter,{'$set':body})
    body = candidateModel.fromdb(body)
    return Response(body)

@api_view(['POST'])
def sendOtp(request):
    systemCheck()
    body = json.loads(request.body.decode('utf-8'))

    otp_filter = {}
    otp_filter['email'] = body['email']
    
    random_number = random.randint(100000, 999999)

    record = MongoMobileApp.find('otps', otp_filter)
    if isinstance(record, list) and len(record)>0:
        try:
            record[0]['otps'].append(random_number)
            setData = {}
            setData['$set'] = {}
            setData['$set']['otps'] = record[0]['otps']
            MongoMobileApp.updateOne('otps', otp_filter, setData)
            sendOtpEmail(random_number,body['email'])
            return Response("Email already exists. Code sent to email : "+ str(body['email']))
        except Exception as error:
            return Response("Internal Server Error")
    else:
        try:
            body['otps'] = []
            body['otps'].append(random_number)
            MongoMobileApp.createOne('otps',body)
            sendOtpEmail(random_number,body['email'])
            return Response("New Email saved. Code sent to email : "+ str(body['email']))
        except Exception as error:
            return Response("Internal Server Error")

@api_view(['POST'])
def verifyOtp(request):
    systemCheck()
    body = json.loads(request.body.decode('utf-8'))
    
    emailFilter = {}
    emailFilter['email'] = body['email']

    record = MongoMobileApp.find('otps', emailFilter)
    if isinstance(record, list) and len(record)>0:
        try:
            otps = record[0]['otps']
            latestCode = otps[-1]
            if str(latestCode) == body['otp']:
                return Response("Code Verification successfull")
            else:
                return Response("Invalid code entered")
        except Exception as error:
            return Response("Internal Server Error")
    else:
        try:
            return Response("No such email " + body['email'] + " exists")
        except Exception as error:
            return Response("Internal Server Error")

@api_view(['POST'])
def registerEvent(request):
    systemCheck()
    body = json.loads(request.body.decode('utf-8'))
    body = registerModel.todb(body)
    print(body)
    event_filter = {}
    event_filter['_id'] = ObjectId(body['eventId'])
    event = MongoMobileApp.find('events', event_filter)
    if isinstance(event, list) and len(event)>0:
        try:
            if event[0]['status'] != "Active":
                return Response("Event diabaled. Contact Administartor")
            else:
                pass
        except Exception as error:
            return Response("Internal Server Error")

    email_Filter = {}
    email_Filter['email'] = {'$regex': f"^{body['email']}$", '$options': 'i'}
    record = MongoMobileApp.find('participants', email_Filter)
    if isinstance(record, list) and len(record)>0:
        msg = "From email"
        print(msg)
        if body['eventId'] not in record[0]['events']:
            body['rollNumber'] = record[0]['rollNumber'] 
            record[0]['events'].append(body['eventId'])
            setData = {}
            setData['$set'] = {}
            setData['$set']['events'] = record[0]['events']
            MongoMobileApp.updateOne('participants', email_Filter, setData)
            event_filter = {}
            event_filter['_id'] = ObjectId(body['eventId'])
            event = MongoMobileApp.find('events', event_filter)
            if isinstance(event, list) and len(event)>0:
                try:
                    event[0]['participants'].append(str(record[0]['_id']))
                    setData = {}
                    setData['$set'] = {}
                    setData['$set']['participants'] = event[0]['participants']
                    MongoMobileApp.updateOne('events', event_filter, setData)
                    print("here1")
                    sendEmail(body)
                    print("here11")
                    return Response("Candidate already registered with email. Event successfully registered")
                except Exception as error:
                    if body['eventId'] in record[0]['events']:
                        index = record[0]['events'].index(body['eventId'])
                        record[0]['events'].pop(index)
                        setData = {}
                        setData['$set'] = {}
                        setData['$set']['events'] = record[0]['events']
                        MongoMobileApp.updateOne('participants', email_Filter, setData)
                        print("here2")
                        return Response("Internal Server Error related to data update")
                    else:
                        print(f"Event ID {body['eventId']} not found in the list.")
                        return Response("Internal Server Error : "+str(error))
            else:
                if body['eventId'] in record[0]['events']:
                    index = record[0]['events'].index(body['eventId'])
                    record[0]['events'].pop(index)
                    setData = {}
                    setData['$set'] = {}
                    setData['$set']['events'] = record[0]['events']
                    MongoMobileApp.updateOne('participants', email_Filter, setData)
                    print("here3")
                    return Response("Internal Server Error related to data update")
                else:
                    print(f"Event ID {body['eventId']} not found in the list.")
                    return Response("Internal Server Error : "+str(error))
        else:
            return Response("Candidate already registered with email. Event is already regeistered")
    else:
        pass

    filter = {}
    filter['name'] = {'$regex': f"^{body['name']}$", '$options': 'i'}
    filter['dateOfBirth'] = body['dateOfBirth']
    filter['fatherName'] = {'$regex': f"^{body['fatherName']}$", '$options': 'i'}
    filter['motherName'] = {'$regex': f"^{body['motherName']}$", '$options': 'i'}
    record = MongoMobileApp.find('participants', filter)
    if isinstance(record, list) and len(record)>0:
        msg = "From details"
        print(msg)
        if body['eventId'] not in record[0]['events']:
            body['rollNumber'] = record[0]['rollNumber'] 
            record[0]['events'].append(body['eventId'])
            setData = {}
            setData['$set'] = {}
            setData['$set']['events'] = record[0]['events']
            MongoMobileApp.updateOne('participants', filter, setData)
            event_filter = {}
            event_filter['_id'] = ObjectId(body['eventId'])
            event = MongoMobileApp.find('events', event_filter)
            if isinstance(event, list) and len(event)>0:
                try:
                    event[0]['participants'].append(str(record[0]['_id']))
                    setData = {}
                    setData['$set'] = {}
                    setData['$set']['participants'] = event[0]['participants']
                    MongoMobileApp.updateOne('events', event_filter, setData)
                    sendEmail(body)
                    return Response("Candidate already registered with details. Event successfully registered")
                except Exception as error:
                    if body['eventId'] in record[0]['events']:
                        index = record[0]['events'].index(body['eventId'])
                        record[0]['events'].pop(index)
                        setData = {}
                        setData['$set'] = {}
                        setData['$set']['events'] = record[0]['events']
                        MongoMobileApp.updateOne('participants', filter, setData)
                        return Response("Internal Server Error related to data update")
                    else:
                        print(f"Event ID {body['eventId']} not found in the list.")
                        return Response("Internal Server Error : "+str(error))
            else:
                if body['eventId'] in record[0]['events']:
                    index = record[0]['events'].index(body['eventId'])
                    record[0]['events'].pop(index)
                    setData = {}
                    setData['$set'] = {}
                    setData['$set']['events'] = record[0]['events']
                    MongoMobileApp.updateOne('participants', filter, setData)
                    return Response("Internal Server Error related to data upadte")
                else:
                    print(f"Event ID {body['eventId']} not found in the list.")
                    return Response("Internal Server Error : "+str(error))
        else:
            return Response("Candidate already registered with details. Event is already registered")
    else:
        print("new candidate")

        current_date = datetime.today().strftime('%y%m')  # Format: YYMM
        allRecords = MongoMobileApp.find('participants', {})
        rollNumber = current_date + str(len(allRecords)+1)
        body['rollNumber'] = rollNumber

        body['events'].append(body['eventId'])
        record = MongoMobileApp.createOne('participants', body)
        event_filter = {}
        event_filter['_id'] = ObjectId(body['eventId'])
        event = MongoMobileApp.find('events', event_filter)
        if isinstance(event, list) and len(event)>0:
            event[0]['participants'].append(str(record))
            setData = {}
            setData['$set'] = {}
            setData['$set']['participants'] = event[0]['participants']
            MongoMobileApp.updateOne('events', event_filter, setData)
            sendEmail(body)
            return Response("New Candidate Registered. Event successfully registered")
        else:
            return Response("Error Occurred")

@api_view(['DELETE'])
def deleteEvent(request):
    systemCheck()
    sts = MobileUser.validate(request.headers)
    if 'isValidRequest' in sts and 'sigVerification' in sts and 'isExpired' in sts and 'isValidToken' in sts:
        if sts['isValidRequest'] == True and sts['sigVerification'] == True and sts['isExpired'] == False and sts['isValidToken'] == True:
            pass
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif 'isValidRequest' in sts and sts['isValidRequest'] == False:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
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

def sendEmail(body):
    sendgrid_api_key = "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"
    sender_email = "karansingh1455@gmail.com"
    recipient_email = body['email']
    subject = "GGSSC - Registration successful "
    emailBody = "Thank you for registration " + "\n\n"

    emailBody += "The details are as follows :\n\n"
    
    emailBody += "Roll Number : " + body['rollNumber'] + "\n"
    emailBody += "Name : " + body['name'] + "\n"
    emailBody += "Event name : " + body['eventName']  + "\n"
    emailBody += "Location : " + body['location']  + "\n\n"

    emailBody += "Waheguru ji ka khalsa waheguru ji ki fateh" + "\n"
    emailBody += "GGSSC Canada"

    try:
        # Create the email content
        message = Mail(
            from_email=sender_email,
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=emailBody
        )
        # Initialize the SendGrid client
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.client.api_keys.get()
        # Send the email
        response = sg.send(message)
        print(f"Email sent successfully! Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def sendOtpEmail(random_number,email):
    sendgrid_api_key = "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"
    sender_email = "karansingh1455@gmail.com"
    recipient_email = email
    subject = "GGSSC verification code"
    emailBody = "Registration Verification code is " + str(random_number)

    try:
        # Create the email content
        message = Mail(
            from_email=sender_email,
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=emailBody
        )
        # Initialize the SendGrid client
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.client.api_keys.get()
        # Send the email
        response = sg.send(message)
        print(f"Email sent successfully! Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def calculate_age(iso_date_str: str) -> int:
    birth_date = datetime.strptime(iso_date_str, "%Y-%m-%d")  # Convert to datetime object
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  # Adjust if birthday hasn't occurred this year
    return age

def calculate_age_2(iso_date_str: str) -> int:
    birth_date = datetime.strptime(iso_date_str, "%Y-%m-%dT%H:%M:%S")  # Convert to datetime object
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  # Adjust if birthday hasn't occurred this year
    return age