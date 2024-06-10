from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(100), nullable=False)
    representante_legal = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(100), nullable=False)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(100), nullable=False)

class Vacante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profesion = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    oferta_economica = db.Column(db.String(50), nullable=False)
    fecha_disponibilidad = db.Column(db.String(50), nullable=False)
