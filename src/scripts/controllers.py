from ast import If
import email
from unicodedata import name
from .query import Query
from flask import request, jsonify, json
import urllib3
http = urllib3.PoolManager()

query_helper = Query()



def get_pasillos():
    try:
        query = query_helper.get_pasillos()
        return jsonify(query)
    except:
        return jsonify("fallo conexion")



