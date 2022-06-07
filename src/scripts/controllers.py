from ast import If
import email
from turtle import update
from unicodedata import name
from .query import Query
from flask import request, jsonify, json
import urllib3
http = urllib3.PoolManager()

query_helper = Query()


def insertPasientes():
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

def getPasientes():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.mostrar(args)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def modificarPacientes():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.modificar("paciente",args ,Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def listaFuntionPaciente():
    if request.method == "POST":
        return insertPasientes()
    elif request.method == "GET":
        return getPasientes()
    elif request.method == "PUT":
        return modificarPacientes()

def insertarDiagnostico():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.insertar("diagnostico",Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def getDiagnosticos():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.buscar("diagnostico",args)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def modificarDiagnostico():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.modificar("diagnostico",args ,Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def listaFuntionDiagnostico():
    if request.method == "POST":
        return insertarDiagnostico()
    elif request.method == "GET":
        return getDiagnosticos()
    elif request.method == "PUT":
        return modificarDiagnostico()

def get_pasillos():
    try:
        query = query_helper.get_pasillos()
        return jsonify(query)
    except:
        return jsonify("fallo conexion")


def doctor():
    try:
        query = query_helper.buscarDoctor()
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
        return especializacionInsert()
    elif request.method == "PUT":
        return especializacionUpdate()