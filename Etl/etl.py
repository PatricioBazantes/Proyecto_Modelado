import pandas as pd
from pymongo import MongoClient
import os
import numpy as np
import re 

# Conexion a la base de datos de mongoDB de origen
client = MongoClient('mongodb://localhost:27020')
db = client['ProyectV1']
collection = db['health']

#Proceso ETL (EXTRACCION)
cursor = collection.find()
df = pd.DataFrame(list(cursor))

# Verificar la conexión exitosa a la base de mongoDB
if client.server_info():
    print("Conexión a la base de datos de origen exitosa.")
else:
    print("La conexión a la base de datos de origen no se pudo establecer.")

# Establecer conexión con MongoDB para guardar los datos
client_save = MongoClient('mongodb://localhost:27025')
db_save = client_save['ProyectV1']
collection_save = db_save['healthRead']

#Proceso ETL (TRANSFORMACION)
# Cambiar el nombre de una columna
df.describe()
df.rename(columns={'seller':'vendedor'}, inplace=True)
df.rename(columns={'index':'indice'}, inplace=True)
df = df.drop(['postalCode', 'nrOfPictures','powerPS','lastSeen','offerType'], axis=1)
df = df.dropna(subset=['brand'])

# Convertir el DataFrame en una lista de diccionarios
data_save = df.to_dict('records')

#Proceso ETL (CARGA DE DATOS)(MONGODB)
collection_save.insert_many(data_save)

# Verificar si los datos han sido modificados y transferidos a la base de mongoDB
if collection_save.count_documents({}) == len(data_save):
    print("Los datos han sido modificados y transferidos con éxito a una base de mongoDB.")
else:
    print("Ocurrió un problema al modificar y transferir los datos.")


# Conexión a MongoDB para realizar la carga de los datos
loadMongoDB = client['ProyectV1']  # Nombre de la base de datos
loadCollection = 'healthRead'  # Nombre de la nueva colección
new_mongodb_collection = loadMongoDB[loadCollection]

if loadCollection in loadMongoDB.list_collection_names():
    # La colección ya existe, actualizar los datos
    for document in df.to_dict('records'):
        filter_query = {'_id': document['_id']}
        new_mongodb_collection.replace_one(filter_query, document, upsert=True)
else:
    # La colección no existe, crearla
    new_mongodb_collection = loadMongoDB.create_collection(loadCollection, capped=False)
    new_mongodb_collection.insert_many(df.to_dict('records'))

# Cerrar la conexión con MongoDB de origen
client.close()



print("Los datos se han transferido con éxito .")



# Guardar los datos transformados en un archivo CSV
file_path = 'C:/data.csv'

if os.path.isfile(file_path):
    # Si el archivo existe, cargar los datos existentes en un DataFrame
    existing_data = pd.read_csv(file_path)

    # Combinar los datos existentes con los nuevos datos
    updated_data = pd.concat([existing_data, df], ignore_index=True)

    # Guardar el DataFrame actualizado en el archivo
    updated_data.to_csv(file_path, index=False)
    
    print("Archivo actualizado exitosamente.")
else:
    # El archivo no existe, descargar o guardar normalmente
    df.to_csv(file_path, index=False)
    print("El archivo no existe. Descargando o guardando normalmente...")
