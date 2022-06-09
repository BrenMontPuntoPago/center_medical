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
        query=query_helper.buscar("paciente",args)
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
        query=query_helper.update("paciente",args ,Data)
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
        query=query_helper.update("diagnostico",args ,Data)
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



def doctor():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"

    try:
        query = query_helper.buscarDoctor(args)
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
        query=query_helper.insertar("doctor",Data)
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
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    try:
        query = query_helper.buscar("especializacion",args)
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
        query=query_helper.insertar("especializacion",Data)
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
def PacDoc():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    try:
        query = query_helper.buscar("paciente_doctor    ",args)
        print(query)
        return jsonify(query)
        
    except:
        return jsonify("fallo conexion")

   
def DocPacInsert():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.insertar("paciente_doctor",Data)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"
        

def DocPacUpdate():
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.update("paciente_doctor",args ,Data)
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
    elif request.method == "GET":
        return especializacion()

def cruDocPac():
    if request.method == "POST":
        return DocPacInsert()
    elif request.method == "PUT":
        return DocPacUpdate()
    elif request.method == "GET":
        return PacDoc()

def dataCompleta():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.buscar("doctor",args)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"

def dataCompletaa():
    try:
        args=list(request.args.items())
    except Exception as e :
        return f"{e}"
    
    try:
        query=query_helper.BuscarPaciente(args)
        return jsonify(query)
    except Exception as e:
        return f" error {e}"
