#!/usr/bin/env python
from ast import Bytes
from base64 import encode
import json
from bson import ObjectId
from uuid import UUID
import datetime
from sortedcontainers import SortedSet
import collections
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, ObjectId):
            return str(obj) 
        elif isinstance(obj, bytes):
            return '' 
        elif isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, SortedSet):
            return encode.cql_encode_tuplestr(obj);
        elif isinstance(obj, collections.Set):
            return dict(_set_object=list(obj))
        return json.JSONEncoder.default(self, obj)