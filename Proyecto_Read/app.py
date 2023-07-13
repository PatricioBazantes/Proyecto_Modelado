from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient, errors
from bson import ObjectId
from pymongo.errors import ConnectionFailure

app = Flask(__name__)
collection = None

def connect_to_alternate_port():
    global collection
    primary_port = 27025
    alternate_ports = [27026, 27027]

    try:
        client = MongoClient(f'mongodb://localhost:{primary_port}/')
        db = client['ProyectV1']
        collection = db['healthRead']
        print(f"Connected to MongoDB on port {primary_port}")
        return collection
    except errors.ConnectionFailure:
        print(f"Failed to connect to MongoDB on port {primary_port}")

    for port in alternate_ports:
        try:
            client = MongoClient(f'mongodb://localhost:{port}/')
            db = client['ProyectV1']
            collection = db['healthRead']
            print(f"Connected to MongoDB on port {port}")
            return collection
        except errors.ConnectionFailure:
            print(f"Failed to connect to MongoDB on port {port}")

    return None

@app.route('/')
def index():
    global collection
    if collection is None:
        collection = connect_to_alternate_port()

    if collection is not None:
        return render_template('index.html', collection=collection)
    else:
        return "No se pudo establecer conexión a ningún puerto de MongoDB"


# Ruta para obtener los datos
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find())
        for item in data:
            item['_id'] = str(item['_id'])
        return jsonify({'status': 'success', 'data': data})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run()
