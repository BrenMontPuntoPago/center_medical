import email
from .connection import Connection
from flask import json
from psycopg2.errors import UniqueViolation


class Query(Connection):

    # --------------- CONSUMO A QUERY DE BASE DE DATOS --------------------

    def doctor(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT * FROM doctor
            INNER JOIN especializacion ON especializacion.fk_doctor_id= doctor.pk_doctor_id
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

    def doctorInsert(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""INSERT INTO public.doctor(
                pk_doctor_id, nombre, apellido)
                VALUES ({datos['pk_doctor_id']}, '{datos['nombre']}', '{datos['apellido']}')
                RETURNING *
                ;
                ;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            print(lista)
            return lista
        except Exception as e:
            print(e)
            return "error doctorInsert"
    def especializacionInsert(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""INSERT INTO public.especializacion(
                pk_esp_id, descripcion, fk_doctor_id)
                VALUES ({datos['pk_esp_id']}, '{datos['descripcion']}', '{datos['pk_doctor_id']}')
                RETURNING *
                ;
                ;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            print(lista)
            return lista
        except Exception as e:
            print(e)
            return "error doctorInsert"

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
    