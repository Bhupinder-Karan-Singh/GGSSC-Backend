import traceback
from urllib.request import urlopen
from .dbconnector import MongoMobileApp
from .jsonutility import JSONEncoder
from datetime import datetime, timedelta, timezone
from django.conf import settings
from base64 import b64decode
import time
import jwt
import firebase_admin
from firebase_admin import credentials, auth

def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None

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

            if not firebase_admin._apps:  # only initialize if no apps exist
                cred = credentials.Certificate("D:\ggssc\ggssc-349bf-firebase-adminsdk-fbsvc-3d3e53da77.json")
                firebase_admin.initialize_app(cred)

            decodedToken = verify_firebase_token(headers['Token'])
            # decodedToken = jwt.decode(headers['Token'], options={"verify_signature": False})
            if not decodedToken:
                print({"error": "Invalid or expired token"})
                retval['code'] = 401
                retval['status'] = False
                retval['jwt'] = None
                retval['isExpired'] = True
                return retval 
            if 'sub' not in decodedToken:
                retval['code'] = 401
                retval['status'] = False
                retval['jwt'] = None
                retval['isExpired'] = True
                return retval    
                        
            retval['sigVerification'] = True  

            try:
                filter = {}
                filter['email'] = decodedToken['email']
                user = MongoMobileApp.find('admin', filter)
                if isinstance(user, list) and len(user)>0:
                    user = user[0]

                    retval['isExpired'] = False
                    retval['isValidToken'] = True
                    
                    return retval
                else:
                    retval['code'] = 401
                    retval['status'] = False
                    retval['jwt'] = None
                    retval['isExpired'] = True
                    retval['isValidToken'] = False
                    return retval
            except:
                print('Error occurred')
                retval['code'] = 500
                retval['status'] = False
                retval['jwt'] = None
                retval['isExpired'] = True
                retval['isValidToken'] = False
                retval['description'] = 'Error occurred'
                return retval

