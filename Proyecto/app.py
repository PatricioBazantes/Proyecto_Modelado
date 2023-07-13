#pip install -U Flask
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient, errors
from bson import ObjectId
from pymongo.errors import ConnectionFailure

app = Flask(__name__)
collection = None

def connect_to_alternate_port():
    global collection
    primary_port = 27020
    alternate_ports = [27021, 27022]

    try:
        client = MongoClient(f'mongodb://localhost:{primary_port}/')
        db = client['ProyectV1']
        collection = db['health']
        print(f"Connected to MongoDB on port {primary_port}")
        return collection
    except errors.ConnectionFailure:
        print(f"Failed to connect to MongoDB on port {primary_port}")

    for port in alternate_ports:
        try:
            client = MongoClient(f'mongodb://localhost:{port}/')
            db = client['ProyectV1']
            collection = db['health']
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

@app.route('/add_data', methods=['POST'])
def add_data():
    global collection
    try:
        data = request.form.to_dict()
        # Asignar _id automáticamente
        data['_id'] = str(ObjectId())
        collection.insert_one(data)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


# Ruta para eliminar datos
@app.route('/delete_data', methods=['POST'])
def delete_data():
    try:
        data = request.json
        timestamps = data['timestamps']
        collection.delete_many({'timestamp': {'$in': timestamps}})
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

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

# Ruta para la vista de creación de documentos
@app.route('/add')
def add_document():
    return render_template('add_document.html')

@app.route('/create_data', methods=['POST'])
def create_data():
    try:
        data = request.form.to_dict()  # Cambiado de request.json a request.form.to_dict()
        # Convertir 'age' a entero
        data['age'] = int(data['age'])
        # Asignar _id automáticamente
        data['_id'] = str(ObjectId())
        collection.insert_one(data)
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


# Ruta para la vista de edición de documentos
@app.route('/edit/<string:timestamp>')
def edit_document(timestamp):
    data = collection.find_one({'_id': ObjectId(timestamp)})
    if data:
        return render_template('edit_document.html', data=data)
    else:
        return jsonify({'status': 'error', 'message': 'Documento no encontrado'})

# Ruta para actualizar documentos
@app.route('/update_data', methods=['POST'])
def update_data():
    try:
        data = request.form.to_dict()
        # Convertir 'age' a entero
        data['age'] = int(data['age'])
        timestamp = data.pop('timestamp')
        collection.update_one({'timestamp': timestamp}, {'$set': data})
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5002)

