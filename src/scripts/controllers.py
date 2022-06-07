from ast import If
import email
from turtle import update
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


def doctor():
    try:
        query = query_helper.doctor()
        print(query)
        return jsonify(query)
        
    except:
        return jsonify("fallo conexion")

def doctorInsert():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.insertar("paciente",Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def doctorUpdate():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.update("doctor",args ,Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def especializacion():
    try:
        query = query_helper.especializacion()
        print(query)
        return jsonify(query)
        
    except:
        return jsonify("fallo conexion")

def especializacionInsert():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.insertar("paciente",Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"
        

def especializacionUpdate():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.update("especializacion",args ,Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"
    
def cruDoctor():
    if request.method == "POST":
        return doctorInsert()
    elif request.method == "GET":
        return doctor()
    elif request.method == "PUT":
        return doctorUpdate()

def cruEspecializacion():
    if request.method == "POST":
        return doctorInsert()
    elif request.method == "GET":
        return doctor()
    elif request.method == "PUT":
        return especializacionUpdate()