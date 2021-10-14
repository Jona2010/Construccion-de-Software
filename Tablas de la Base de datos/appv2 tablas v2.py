from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#posgresql
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:290519@127.0.0.1:8080/proyectocs"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # par q no de warnings

db = SQLAlchemy(app)
ma = Marshmallow(app)

#tabla usuario
class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuarionombre = db.Column(db.String(100))
    usuarioapellidos = db.Column(db.String(100))
    usuariodni = db.Column(db.Integer)
    usuariodireccion = db.Column(db.String(100))
    usuarioedad = db.Column(db.Integer)
    usuariofechanacimiento = db.Column(db.Date)
    usuariodniemision = db.Column(db.Date)
    usuariogenero = db.Column(db.String(100))
    usuarioalias = db.Column(db.String(100))
    usuariocontraseña = db.Column(db.String(100))
    usuarioemail = db.Column(db.String(100))

    def __init__(self, usuarionombre, usuarioapellidos, usuariodni, usuariodireccion, usuarioedad, usuariofechanacimiento
        , usuariodniemision, usuariogenero, usuarioalias, usuariocontraseña, usuarioemail):
        self.usuarionombre = usuarionombre
        self.usuarioapellidos = usuarioapellidos
        self.usuariodni = usuariodni
        self.usuariodireccion = usuariodireccion
        self.usuarioedad = usuarioedad
        self.usuariofechanacimiento = usuariofechanacimiento
        self.usuariodniemision = usuariodniemision
        self.usuariogenero = usuariogenero
        self.usuarioalias = usuarioalias
        self.usuariocontraseña = usuariocontraseña
        self.usuarioemail = usuarioemail

db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuarionombre', 'usuarioapellidos', 'usuariodni', 'usuariodireccion', 'usuarioedad',
            'usuariofechanacimiento', 'usuariodniemision', 'usuariogenero', 'usuarioalias', 'usuariocontraseña',
            'usuarioemail')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

#tabla candidato
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

#tabla votante
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

#tabla voto
class voto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuariovoto = db.Column(db.String(100))
    partidovoto = db.Column(db.String(100))
    fechavoto = db.Column(db.DateTime)
    lugarvoto = db.Column(db.String(100))

    def __init__(self, usuariovoto, partidovoto, fechavoto, lugarvoto):
        self.usuariovoto = usuariovoto
        self.partidovoto = partidovoto
        self.fechavoto = fechavoto
        self.lugarvoto = lugarvoto

db.create_all() # crea todas las tablas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuariovoto', 'partidovoto', 'fechavoto', 'lugarvoto')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
