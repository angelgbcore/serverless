from pymongo import MongoClient
import json

# establish connex
conn = MongoClient('localhost', 27017)
conn = MongoClient()
print ('conectado...' + conn)

# create db
db = conn.baseDeDatos

# create collection
collection = db.InfoDeNotebooks

# <-------------------------------------------------------- INSERT 
# Funciones para insertar datos
def insertDatosNotebook(NBDataconFecha) :
    """
    Una vez que se agrego fecha y hora en la NBDataconFecha recibida por POST
    agregamos el documento "registro"  en la base de datos.
    """
    insertNotebook = collection.insert(NBDataconFecha)