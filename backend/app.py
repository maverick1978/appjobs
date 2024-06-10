
from flask import Flask, render_template, request, jsonify, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import os
print("Current working directory:", os.getcwd())

app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def home():
    return render_template('index.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appjobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelos
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_empresa = db.Column(db.String(100), nullable=False)
    representante_legal = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(60), nullable=False)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(60), nullable=False)

# Crear base de datos y usuarios iniciales
@app.before_request
def create_tables():
    db.create_all()
    if not Empresa.query.filter_by(correo='correo@empresa.con').first():
        hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
        empresa = Empresa(
            nombre_empresa='empresa',
            representante_legal='Representante Legal',
            direccion='Direccion Empresa',
            telefono='1234567890',
            correo='correo@empresa.con',
            clave=hashed_password
        )
        db.session.add(empresa)
        db.session.commit()

    if not Persona.query.filter_by(correo='correo@persona.com').first():
        hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
        persona = Persona(
            correo='correo@persona.com',
            clave=hashed_password
        )
        db.session.add(persona)
        db.session.commit()

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_empresa', methods=['POST'])
def register_empresa():
    data = request.form
    if not data['correo'] or not data['clave']:
        return jsonify({'error': 'Correo y clave son requeridos'}), 400

    if Empresa.query.filter_by(correo=data['correo']).first():
        return jsonify({'error': 'El correo ya está registrado'}), 400

    hashed_password = bcrypt.generate_password_hash(data['clave']).decode('utf-8')

    empresa = Empresa(
        nombre_empresa=data['nombre_empresa'],
        representante_legal=data['representante_legal'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        correo=data['correo'],
        clave=hashed_password
    )
    db.session.add(empresa)
    db.session.commit()
    return jsonify({'message': 'Empresa registrada exitosamente'})

@app.route('/empresa')
def empresa():
    return render_template('empresa.html')

@app.route('/persona')
def persona():
    return render_template('persona.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Devuelve una respuesta vacía y sin contenido
if __name__ == '__main__':
    print("Current working directory:", os.getcwd())  # Verifica el directorio de trabajo actual
    app.run(debug=True)