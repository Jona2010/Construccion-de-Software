from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#libraries: pip3 install flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy pymysql

app = Flask(__name__)

# para que postgresql funcione
#sudo pip3 install psycopg2-binary

# mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:290519@127.0.0.1:3306/flaskmysql'

#posgresql
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:290519@127.0.0.1:8080/proyectocs"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # par q no de warnings

db = SQLAlchemy(app)
ma = Marshmallow(app)

# tabla candidato
class candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidatepartido = db.Column(db.String(100))
    candidateimagen = db.Column(db.String(100))
    candidateocupacion = db.Column(db.String(100))
    candidatesentencias = db.Column(db.String(100))

    def __init__(self, candidatepartido, candidateimagen, candidateocupacion, candidatesentencias):
        self.candidatepartido = candidatepartido
        self.candidateimagen = candidateimagen
        self.candidateocupacion = candidateocupacion
        self.candidatesentencias = candidatesentencias

db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'candidatepartido', 'candidateimagen', 'candidateocupacion', 'candidatesentencias')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# tabla votante
class votante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerosala = db.Column(db.Integer)
    numeromesa = db.Column(db.Integer)
    numeroorden = db.Column(db.Integer)
    localdevotacion = db.Column(db.String(100))
    votantefoto = db.Column(db.String(100))

    def __init__(self, numerosala, numeromesa, numeroorden, localdevotacion, votantefoto):
        self.numerosala = numerosala
        self.numeromesa = numeromesa
        self.numeroorden = numeroorden
        self.localdevotacion = localdevotacion
        self.votantefoto = votantefoto

db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'numerosala', 'numeromesa', 'numeroorden', 'localdevotacion', 'votantefoto')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/create_task', methods=['POST'])
def create_task():
    print(request.json)

    title = request.json['title']
    description = request.json['description']

    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task) # respondemos cpon la tarea creada

@app.route('/tasks', methods=['POST'])
def tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks) # lo vuelve serializable
    return jsonify(result)


@app.route('/task/<id>', methods=['POST'])
def task(id):
    result = Task.query.get(id)
    result = task_schema.dump(result) # lo vuelve serializable
    return jsonify(result)

@app.route('/update_task/<id>', methods=['POST'])
def update_task(id):
    task = Task.query.get(id)
    title = request.json['title']
    description = request.json['description']

    task.title = title
    task.description = description

    db.session.commit()
    return task_schema.jsonify(task)


@app.route('/delete_task/<id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
