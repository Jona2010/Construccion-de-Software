from flask import Flask
from flask import request
from flask import jsonify
import psycopg2

#libraries: sudo pip3 install psycopg2-binary

app = Flask(__name__)

conn = psycopg2.connect(
    host="127.0.0.1",
    port="8080",
    database="pruebaproyecto",
    user="postgres",
    password="290519")

cursor = conn.cursor()

#Creando un candidato
@app.route('/create_candidate', methods=['POST'])
def create_candidate():
    print(request.json)

    params = {
        'candidatepartido' : request.json['candidatepartido'],
        'candidateimagen' : request.json['candidateimagen'],
        'candidateocupacion' : request.json['candidateocupacion'],
        'candidatesentencias' : request.json['candidatesentencias'],
    }

    query = """insert into candidato (candidatepartido, candidateimagen, candidateocupacion, candidatesentencias) 
         values (%(candidatepartido)s, %(candidateimagen)s, %(candidateocupacion)s,  %(candidatesentencias)s) RETURNING id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {'id': id_of_new_row, 'candidatepartido': params['candidatepartido'], 'candidateimagen': params['candidateimagen'],
    'candidateocupacion': params['candidateocupacion'], 'candidatesentencias': params['candidatesentencias']}
    return jsonify(content)

#Creando un votante
@app.route('/create_votante', methods=['POST'])
def create_votante():
    print(request.json)

    params = {
        'numerosala' : request.json['numerosala'],
        'numeromesa' : request.json['numeromesa'],
        'numeroorden' : request.json['numeroorden'],
        'localdevotacion' : request.json['localdevotacion'],
        'votantefoto' : request.json['votantefoto']
    }

    query = """insert into votante (numerosala, numeromesa, numeroorden, localdevotacion, votantefoto) 
         values (%(numerosala)s, %(numeromesa)s, %(numeroorden)s, %(localdevotacion)s, %(votantefoto)s) RETURNING id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {'id': id_of_new_row, 'numerosala': params['numerosala'], 'numeromesa': params['numeromesa'],
    'numeroorden': params['numeroorden'], 'localdevotacion': params['localdevotacion'], 'votantefoto': params['votantefoto']}
    return jsonify(content)

@app.route('/tasks', methods=['POST'])
def tasks():
    cursor.execute("SELECT * from task")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'title': result[1], 'description': result[2]}
        data.append(content)
        content = {}
    return jsonify(data)


@app.route('/task/<id>', methods=['POST'])
def task(id):
    cursor.execute("SELECT * from task where id="+id)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'title': result[1], 'description': result[2]}
        data.append(content)
        content = {}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)