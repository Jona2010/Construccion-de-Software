from flask import Flask
from flask import request
from flask import jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="127.0.0.1",
    port="8080",
    database="pruebaproyecto",
    user="postgres",
    password="290519")

cursor = conn.cursor()

#Creando un usuario
@app.route('/create_usuario', methods=['POST'])
def create_usuario():
    print(request.json)

    params = {
        'usuarionombre' : request.json['usuarionombre'],
        'usuarioapellidos' : request.json['usuarioapellidos'],
        'usuariodni' : request.json['usuariodni'],
        'usuariodireccion' : request.json['usuariodireccion'],
        'usuarioedad' : request.json['usuarioedad'],
        'usuariofechanacimiento' : request.json['usuariofechanacimiento'],
        'usuariodniemision' : request.json['usuariodniemision'],
        'usuariogenero' : request.json['usuariogenero'],
        'usuarioalias' : request.json['usuarioalias'],
        'usuariocontraseña' : request.json['usuariocontraseña'],
        'usuarioemail' : request.json['usuarioemail']
    }

    query = """insert into usuario (usuarionombre, usuarioapellidos, usuariodni, usuariodireccion, usuarioedad, 
    usuariofechanacimiento, usuariodniemision, usuariogenero, usuarioalias, usuariocontraseña,usuarioemail)
         values (%(usuarionombre)s, %(usuarioapellidos)s, %(usuariodni)s, %(usuariodireccion)s, %(usuarioedad)s,
         %(usuariofechanacimiento)s, %(usuariodniemision)s, %(usuariogenero)s, %(usuarioalias)s, %(usuariocontraseña)s,
         %(usuarioemail)s) 
         RETURNING id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {'id': id_of_new_row, 'usuarionombre': params['usuarionombre'], 'usuarioapellidos': params['usuarioapellidos'],
    'usuariodni': params['usuariodni'], 'usuariodireccion': params['usuariodireccion'], 'usuarioedad': params['usuarioedad'],
    'usuariofechanacimiento': params['usuariofechanacimiento'], 'usuariodniemision': params['usuariodniemision'],
    'usuariogenero': params['usuariogenero'], 'usuarioalias': params['usuarioalias'], 'usuariocontraseña': params['usuariocontraseña'],
    'usuarioemail': params['usuarioemail']}
    return jsonify(content)

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

#Buscando a un usuario mediante el DNI
@app.route('/user/<usuariodni>', methods=['POST'])
def user(usuariodni):
    cursor.execute("SELECT * from usuario where usuariodni="+usuariodni)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'usuarionombre': result[1], 'usuarioapellidos': result[2], 'usuariodni': result[3], 'usuariodireccion':
        result[4], 'usuarioedad': result[5], 'usuariofechanacimiento': result[6], 'usuariodniemision': result[7], 'usuariogenero': result[8],
        'usuarioalias': result[9], 'usuariocontraseña': result[10], 'usuarioemail': result[11]}
        data.append(content)
        content = {}
    return jsonify(data)

#Buscando a un candidato por su ocupacion
@app.route('/candidate/<candidateocupacion>', methods=['POST'])
def candidate(candidateocupacion):
    cursor.execute("SELECT * from candidato where candidateocupacion="+candidateocupacion)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'candidatepartido': result[1], 'candidateimagen': result[2], 'candidateocupacion': result[3], 
        'candidatesentencias': result[4]}
        data.append(content)
        content = {}
    return jsonify(data)

#Buscando el numero de mesa de un votante
@app.route('/votante/<numeromesa>', methods=['POST'])
def votante(numeromesa):
    cursor.execute("SELECT * from votante where numeromesa="+numeromesa)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'id': result[0], 'numerosala': result[1], 'numeromesa': result[2], 'numeroorden': result[3], 'localdevotacion':
        result[4], 'votantefoto': result[5]}
        data.append(content)
        content = {}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)