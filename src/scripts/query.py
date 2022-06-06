import email
from .connection import Connection
from flask import json
from psycopg2.errors import UniqueViolation


class Query(Connection):

    # --------------- CONSUMO A QUERY DE BASE DE DATOS --------------------

    def placeHolder(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT *
FROM datos
INNER JOIN address ON address.fk_id_datos= datos.pk_id_datos
INNER JOIN company ON company.fk_id_datos= datos.pk_id_datos
INNER JOIN geo ON geo.fk_address= address.pk_address

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

    def placeHolderInsert(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""INSERT INTO public.datos(
                pk_id_datos, name, username, email, phone, website)
                VALUES ({datos['id']}, '{datos['name']}', '{datos['username']}', '{datos['email']}', '{datos['phone']}', '{datos['website']}')
                RETURNING *
                ;
                ;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            #resp = cursor.row_factory
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            print(lista)
            return lista
        except Exception as e:
            print(e)
            return "error placeHolderInsert"

    def placeHolderInsertAddres(self, datos):
            cnx = self.connect()
            cursor = cnx.cursor()
            # Define el inicio de la query
            try:
                query = f"""INSERT INTO public.address(
	                pk_address, street, suite, city, zipcode, fk_id_datos)
                    VALUES ({datos['id']}, '{datos['street']}', '{datos['suite']}', '{datos['city']}', {datos['zipcode']}, {datos['pk_id_datos']})
                    RETURNING *
                    ;
                    ;"""
                print(query)
                cursor.execute(query)
                cnx.commit()
                #resp = cursor.row_factory
                lista = [dict((cursor.description[i][0], value)
                            for i, value in enumerate(row)) for row in cursor.fetchall()]
                self.closeConnection(cnx)
                return lista
            except Exception as e:
                print(e)
                return "prueba"

    def placeHolderInsertGeo(self, datos):
            cnx = self.connect()
            cursor = cnx.cursor()
            # Define el inicio de la query
            try:
                query = f"""INSERT INTO public.geo(
	                pk_geo, lat, lng, fk_address)
                    VALUES ({datos['id']},  {datos['lat']}, {datos['lng']}, {datos['pk_address']})
                    RETURNING *
                    ;
                    ;"""
                print(query)
                cursor.execute(query)
                cnx.commit()
                #resp = cursor.row_factory
                lista = [dict((cursor.description[i][0], value)
                            for i, value in enumerate(row)) for row in cursor.fetchall()]
                self.closeConnection(cnx)
                return lista
            except Exception as e:
                print(e)
                return "prueba"

    def placeHolderInsertCompany(self, datos):
            cnx = self.connect()
            cursor = cnx.cursor()
            # Define el inicio de la query
            try:
                query = f"""INSERT INTO public.company(
	                pk_company, name, catchphrase, bs, fk_id_datos)
                    VALUES ({datos['id']},  '{datos['nameCompany']}', '{datos['catchphrase']}', '{datos['bs']}',{datos['pk_id_datos']})
                    RETURNING *
                    ;
                    ;"""
                print(query)
                cursor.execute(query)
                cnx.commit()
                #resp = cursor.row_factory
                lista = [dict((cursor.description[i][0], value)
                            for i, value in enumerate(row)) for row in cursor.fetchall()]
                self.closeConnection(cnx)
                return lista
            except Exception as e:
                print(e)
                return "prueba"

    def placeHolderUpdate(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        print(datos)

        try:

            query = f"""UPDATE public.datos
	                SET """
            recorrido= len(datos)-1
            print(recorrido)
            for key, dato in enumerate(datos):
                query += f"""{dato}='{datos[dato]}'"""
                if(key!=recorrido):
                    query+=','
            query +=f""" WHERE pk_id_datos={datos['pk_id_datos']} RETURNING*;;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "No esta retornando los valores"
    def placeHolderUpdateGeo(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        print(datos)

        try:

            query = f"""UPDATE public.geo
	                SET """
            
            recorrido= len(datos)-1
            print(recorrido)
            for key, dato in enumerate(datos):
                query += f"""{dato}='{datos[dato]}'"""
                if(key!=recorrido):
                    query+=','
            query +=f""" WHERE pk_geo={datos['pk_geo']} RETURNING*;;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "No esta retornando los valores"

    def placeHolderUpdateCompany(self, datos):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        print(datos)

        try:
            query = f"""UPDATE public.company
	                SET """
            
            recorrido= len(datos)-1
            print(recorrido)
            for key, dato in enumerate(datos):
                query += f"""{dato}='{datos[dato]}'"""
                if(key!=recorrido):
                    query+=','
            query +=f""" WHERE pk_company={datos['pk_company']} RETURNING*;;"""
            print(query)
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "No esta retornando los valores"

    def get_pasillos(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT * FROM pasillos"""

            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"

    def get_sub_pasillos(self, idPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query = f"""SELECT * FROM subpasillos WHERE idpasillo = {idPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"

    def get_productos_sub_pasillos(self, idSubPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query = f"""SELECT p.idproducto, p.titulo, p.descripcion, p.precio, p.img FROM productos p
            JOIN subpasillo_productos ON subpasillo_productos.idproducto = p.idproducto
            WHERE subpasillo_productos.idsubpasillo = {idSubPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"

    def get_productos_pasillos(self, idPasillo):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query = f"""SELECT p.idproducto, p.titulo, p.descripcion, p.precio, p.img FROM productos p
            JOIN subpasillo_productos ON subpasillo_productos.idproducto = p.idproducto
            JOIN subpasillos ON subpasillos.idsubpasillo = subpasillo_productos.idsubpasillo
            WHERE subpasillos.idpasillo = {idPasillo}"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value)
                          for i, value in enumerate(row)) for row in cursor.fetchall()]
            print(lista)
            self.closeConnection(cnx)
            return lista
        except Exception as e:
            print(e)
            return "prueba"

    def mostrar(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        # Define el inicio de la query
        try:
            query = f"""SELECT *
FROM paciente
INNER JOIN  diagnostico ON diagnostico.fk_pac_id= paciente.pk_pac_id
INNER JOIN paciente_doctor ON paciente_doctor.pk_pac_id= paciente.pk_pac_id
INNER JOIN doctor ON paciente_doctor.pk_doctor_id= doctor.pk_doctor_id
INNER JOIN especializacion ON especializacion.fk_doctor= doctor.pk_doctor_id

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

    def modificar(self, tabla,datosBuscar, datoModificar):
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