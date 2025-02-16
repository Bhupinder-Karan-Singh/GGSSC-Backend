import traceback
from urllib.request import urlopen
from .dbconnector import MongoMobileApp
from .jsonutility import JSONEncoder
from datetime import datetime, timedelta, timezone
from django.conf import settings
from base64 import b64decode
import time
from cryptography.hazmat.primitives import serialization
import jwt

class MobileUser:
    def __init__(self):
        pass

    @classmethod
    def validate(self, headers):
        retval = {}
        if 'Token' not in headers:
            retval['sigVerification'] = False
            retval['isValidRequest'] = False
            return retval; 
        else:
            retval['isValidRequest'] = True
            decodedToken = jwt.decode(headers['Token'], options={"verify_signature": False})
            if 'sub' not in decodedToken:
                retval['code'] = 401
                retval['status'] = False
                retval['jwt'] = None
                retval['description'] = 'Signature Expired'
                return retval                
            retval['sigVerification'] = True    
            try:
                filter = {}
                filter['email'] = decodedToken['email']
                user = MongoMobileApp.find('users', filter)
                if isinstance(user, list) and len(user)>0:
                    user = user[0]
                    retval['isExpired'] = False
                    retval['isValidToken'] = True
                    return retval
                else:
                    retval['code'] = 401
                    retval['status'] = False
                    retval['jwt'] = None
                    retval['description'] = 'Unknown User'
                    return retval
            except:
                print('Verified against DB privileges')
                filter = {}
                filter['email'] = decodedToken['email']
                user = MongoMobileApp.find('uma-userprofile', filter)
                if isinstance(user, list) and len(user)>0:
                    user = user[0]
                    retval['isExpired'] = False
                    retval['isValidToken'] = True
                    return retval
                else:
                    retval['code'] = 401
                    retval['status'] = False
                    retval['jwt'] = None
                    retval['description'] = 'Unknown User'
                    return retval

