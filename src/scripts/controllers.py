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
        resp= {}
        datos= request.json
        if (datos):
            doctor = query_helper.doctorInsert(datos)
            if(doctor>0):
                resp = {"doctor": doctor[0]}
                datos['pk_doctor_id'] = doctor[0]['pk_doctor_id']
                especializacion = query_helper.especializacionInsert(datos)
                if (especializacion>0):
                    resp = { **resp, especializacion:especializacion[0]}
                    datos['pk_esp_id'] = especializacion[0]['pk_esp_id']
        return jsonify(resp)
    except:
        return  print('Falla de query Insert')

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
        return doctorUpdate(), especializacionUpdate()
       

