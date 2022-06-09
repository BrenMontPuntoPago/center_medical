import email
from .connection import Connection
from flask import json
from psycopg2.errors import UniqueViolation


class Query(Connection):

    # --------------- CONSUMO A QUERY DE BASE DE DATOS --------------------

    def BuscarPaciente(self, datosBuscar):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT * FROM paciente
            INNER JOIN paciente_doctor ON paciente_doctor.pk_pac_id= paciente.pk_paciente_id
            INNER JOIN doctor ON paciente_doctor.pk_doctor_id= doctor.pk_doctor_id 
            {f" WHERE paciente.{datosBuscar[0][0]} = '{str(datosBuscar[0][1])}'" if datosBuscar else "" } ;"""
            # query= f"""SELECT * FROM paciente {f" WHERE {datosBuscar[0][0]} = '{str(datosBuscar[0][1])}'" if datosBuscar else "" }"""
            
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return f"prueba {e}"
            
    def buscarDoctor(self, datosBuscar):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT *
            FROM doctor
            FULL JOIN especializacion ON especializacion.fk_doctor= doctor.pk_doctor_id
            {f" WHERE doctor.{datosBuscar[0][0]} = '{str(datosBuscar[0][1])}'" if datosBuscar else "" }
            ;"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"

    def buscar(self, tabla,datosBuscar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT * FROM {tabla} {f" WHERE {datosBuscar[0][0]} = '{str(datosBuscar[0][1])} '" if datosBuscar else "" } """
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "error prueba"

    def insertar(self, tabla ,datoModificar):
        cnx = self.connect()
        cursor = cnx.cursor()
        var=list(datoModificar)
        datos=[]
        for k in datoModificar:
            datos.append(str(datoModificar[str(k)]))

        var_text=", ".join(var)
        datos_text="','".join(datos)
 
        try:
            query= f""" INSERT INTO {tabla} ({var_text}) VALUES ('{datos_text}') RETURNING * ;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return f"error {e}"

    def update(self, tabla,datosBuscar, datoModificar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            for k in datoModificar:
                query= f""" UPDATE {tabla} SET  {  f"{k} = '{str(datoModificar[str(k)])}'"}   WHERE {datosBuscar[0][0]} = {datosBuscar[0][1]} RETURNING * ;"""
                print(query)
                cursor.execute(query)
                cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return f"error {e}"
    