from ast import If
import email
from unicodedata import name
from .query import Query
from flask import request, jsonify, json
import urllib3
http = urllib3.PoolManager()

query_helper = Query()

data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
        }
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
        }
    },
    {
        "id": 4,
        "name": "Patricia Lebsack",
        "username": "Karianne",
        "email": "Julianne.OConner@kory.org",
        "address": {
            "street": "Hoeger Mall",
            "suite": "Apt. 692",
            "city": "South Elvis",
            "zipcode": "53919-4257",
            "geo": {
                "lat": "29.4572",
                "lng": "-164.2990"
            }
        },
        "phone": "493-170-9623 x156",
        "website": "kale.biz",
        "company": {
            "name": "Robel-Corkery",
            "catchPhrase": "Multi-tiered zero tolerance productivity",
            "bs": "transition cutting-edge web services"
        }
    },
    {
        "id": 5,
        "name": "Chelsey Dietrich",
        "username": "Kamren",
        "email": "Lucio_Hettinger@annie.ca",
        "address": {
            "street": "Skiles Walks",
            "suite": "Suite 351",
            "city": "Roscoeview",
            "zipcode": "33263",
            "geo": {
                "lat": "-31.8129",
                "lng": "62.5342"
            }
        },
        "phone": "(254)954-1289",
        "website": "demarco.info",
        "company": {
            "name": "Keebler LLC",
            "catchPhrase": "User-centric fault-tolerant solution",
            "bs": "revolutionize end-to-end systems"
        }
    },
    {
        "id": 6,
        "name": "Mrs. Dennis Schulist",
        "username": "Leopoldo_Corkery",
        "email": "Karley_Dach@jasper.info",
        "address": {
            "street": "Norberto Crossing",
            "suite": "Apt. 950",
            "city": "South Christy",
            "zipcode": "23505-1337",
            "geo": {
                "lat": "-71.4197",
                "lng": "71.7478"
            }
        },
        "phone": "1-477-935-8478 x6430",
        "website": "ola.org",
        "company": {
            "name": "Considine-Lockman",
            "catchPhrase": "Synchronised bottom-line interface",
            "bs": "e-enable innovative applications"
        }
    },
    {
        "id": 7,
        "name": "Kurtis Weissnat",
        "username": "Elwyn.Skiles",
        "email": "Telly.Hoeger@billy.biz",
        "address": {
            "street": "Rex Trail",
            "suite": "Suite 280",
            "city": "Howemouth",
            "zipcode": "58804-1099",
            "geo": {
                "lat": "24.8918",
                "lng": "21.8984"
            }
        },
        "phone": "210.067.6132",
        "website": "elvis.io",
        "company": {
            "name": "Johns Group",
            "catchPhrase": "Configurable multimedia task-force",
            "bs": "generate enterprise e-tailers"
        }
    },
    {
        "id": 8,
        "name": "Nicholas Runolfsdottir V",
        "username": "Maxime_Nienow",
        "email": "Sherwood@rosamond.me",
        "address": {
            "street": "Ellsworth Summit",
            "suite": "Suite 729",
            "city": "Aliyaview",
            "zipcode": "45169",
            "geo": {
                "lat": "-14.3990",
                "lng": "-120.7677"
            }
        },
        "phone": "586.493.6943 x140",
        "website": "jacynthe.com",
        "company": {
            "name": "Abernathy Group",
            "catchPhrase": "Implemented secondary concept",
            "bs": "e-enable extensible e-tailers"
        }
    },
    {
        "id": 9,
        "name": "Glenna Reichert",
        "username": "Delphine",
        "email": "Chaim_McDermott@dana.io",
        "address": {
            "street": "Dayna Park",
            "suite": "Suite 449",
            "city": "Bartholomebury",
            "zipcode": "76495-3109",
            "geo": {
                "lat": "24.6463",
                "lng": "-168.8889"
            }
        },
        "phone": "(775)976-6794 x41206",
        "website": "conrad.com",
        "company": {
            "name": "Yost and Sons",
            "catchPhrase": "Switchable contextually-based project",
            "bs": "aggregate real-time technologies"
        }
    },
    {
        "id": 10,
        "name": "Clementina DuBuque",
        "username": "Moriah.Stanton",
        "email": "Rey.Padberg@karina.biz",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {
                "lat": "-38.2386",
                "lng": "57.2232"
            }
        },
        "phone": "024-648-3804",
        "website": "ambrose.net",
        "company": {
            "name": "Hoeger LLC",
            "catchPhrase": "Centralized empowering task-force",
            "bs": "target end-to-end models"
        }
    }
]

url= 'https://jsonplaceholder.typicode.com/users'



def getDataFiltered(username, email,id):
    lista=[]
    if not username and not email and not id:
        return data


    for _, value in enumerate(data):
        if (email and value['email'] == email):
            lista.append(value)
        elif (username and value['username'] == username):
            lista.append(value)
        elif (id and value['id'] == int(id)):
            lista.append(value)

    return lista

def usersLocal():
    try:
        username = request.json.get("username","")
        email = request.json.get("email","")
        id = request.json.get("id","")
        return jsonify(getDataFiltered(username,email,id)) 
    except Exception as be:
      print ("Error:" + " " + str(be))
    return ("Error:" + " " + str(be))

     
def users():
    try:
        if(request.method=='POST'):
            filter = request.args.to_dict()
            respuesta= request.json
            r = http.request(
                'GET', 
                url,
                fields=respuesta
                )
            filter= json.loads(r.data.decode('utf8'))
            return jsonify(filter)

    except:
        print('falla')
    return 'sss'

places= [
        {
            "name": "Exito del norte",
            "geometry": [
                4.7210257,
                -74.1267725
            ]
        },
        {
            "name": "Reval de la 68",
            "geometry": [
                4.6417536,
                -74.1157099
            ]
        },
        {
            "name": "Reval Soacha",
            "geometry": [
                4.5948366,
                -74.191671
            ]
        }
    ]

def getPlacesFiltered(name):
    if not name:
        return places
    print(name)
    lugar=[]
    for _, value in enumerate(places):
        if (name and value['name'] == name):
            lugar.append(value)

    return lugar

def maps():
    try:
        name = request.args.get("name", "")
        return jsonify(getPlacesFiltered(name)) 
    except:
      print ('Esta ocurriendo un error')
    return 'Esta ocurriendo un error'

def transponer(m):
    matrizS = ""
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
        matrizS += str(t[i])+'\n'
    return matrizS


def mock():
    try:
        # query = query_helper.get_pasillos()
        matrizPost = request.json["matriz"]
        print(matrizPost)
        transpuesta = transponer(matrizPost)

        return (transpuesta)
    except:
        print("fallo")
    # if(request.method == "POST"):
    #     print(222)
    # nombre = request.args.get('nombre',"paco")
    # json = request.json['json']

    return "sss"


def mock2():
    return "hola mundo mock 2"


def placeHolder():
    try:
        query = query_helper.placeHolder()
        return jsonify(query)
    except:
        return jsonify("Fallo query")
     
def placeHolderInsert():
    try:
        datos= request.json
        user = query_helper.placeHolderInsert(datos)
        datos['pk_id_datos'] = user[0]['pk_id_datos']
        address = query_helper.placeHolderInsertAddres(datos)
        datos['pk_address'] = address[0]['pk_address']
        geo = query_helper.placeHolderInsertGeo(datos)
        company = query_helper.placeHolderInsertCompany(datos)


        resp = {**user[0], **address[0], **geo[0], **company[0]}
       
        return jsonify(resp)
    except Exception as e:
        print(e)
        return  print('Falla de query Insert')
           
def placeHolderUpdate():
    try:
        datos= request.json
        if("datos" in datos):
            query = query_helper.placeHolderUpdate(datos["datos"])
        if("geo" in datos):
            query = query_helper.placeHolderUpdateGeo(datos["geo"])
        if("company" in datos):
            query = query_helper.placeHolderUpdateCompany(datos["company"])
        return jsonify(query)
       
    except Exception as e:
        print(e)
        return  print('Falla de query Update')

def get_pasillos():
    try:
        query = query_helper.get_pasillos()
        return jsonify(query)
    except:
        return jsonify("fallo conexion")
    # obj = [{'img': 'https://d50xhnwqnrbqk.cloudfront.net/featured/web/a4cf85a23b9d5ade6ef19e9835038781.jpg', 'titulo': 'Navidad'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/a02b5c8924c4d79a4caa6f47b3e89bd6.png', 'titulo': 'Lacteos'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/e310a83bd35f77683f5d78c86c9a9319.png', 'titulo': 'Carnes'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/065d0d7967f6eb5c36e23793a267265e.png', 'titulo': 'Galletas'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/a02b5c8924c4d79a4caa6f47b3e89bd6.png', 'titulo': 'Pasteleria'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/e310a83bd35f77683f5d78c86c9a9319.png', 'titulo': 'Aceites'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/featured/web/a4cf85a23b9d5ade6ef19e9835038781.jpg', 'titulo': 'Arroces'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/6f3f0c6f36df4a3d7396c40a9a5f4f6f.png', 'titulo': 'Pastas'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/59902a4d93a37e24c1ca10486f2745b2.png', 'titulo': 'Vegetales'}]
    # return jsonify(
    #     obj
    # )


def get_sub_pasillos():
    idPasillo = request.args.get('idPasillo', "")
    try:
        query = query_helper.get_sub_pasillos(idPasillo)
        return jsonify(query)
    except:
        return jsonify("fallo conexion")


def get_productos_sub_pasillos():
    idSubPasillo = request.args.get('idSubPasillo', "")
    try:
        query = query_helper.get_productos_sub_pasillos(idSubPasillo)
        return jsonify(query)
    except:
        return jsonify("fallo conexion")


def get_productos_pasillos():
    idPasillo = request.args.get('idPasillo', "")
    try:
        query = query_helper.get_productos_pasillos(idPasillo)
        return jsonify(query)
    except:
        return jsonify("fallo conexion")
