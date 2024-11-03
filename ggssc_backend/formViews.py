import collections
from django.conf import settings
from .dbconnector import MongoMobileApp
from rest_framework.decorators import api_view

def systemCheck():
    collections = MongoMobileApp.listCollections()
    if  'events' not in collections:
        MongoMobileApp.createCollection('events') 
    return True

@api_view(['POST'])
def createForm(request):
    body = json.loads(request.body.decode('utf-8'))
    print(body)