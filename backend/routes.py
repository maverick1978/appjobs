from flask import Blueprint, request, jsonify, render_template
from models import db, Empresa, Persona, Vacante
from flask_bcrypt import Bcrypt

main_routes = Blueprint('main_routes', __name__)

bcrypt = Bcrypt()

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/register_empresa', methods=['POST'])
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

@main_routes.route('/create_vacancy', methods=['POST'])
def create_vacancy():
    data = request.form
    vacante = Vacante(
        profesion=data['profession'],
        descripcion=data['description'],
        oferta_economica=data['salary'],
        fecha_disponibilidad=data['availabilityDate']
    )
    db.session.add(vacante)
    db.session.commit()
    return jsonify({'message': 'Vacante creada exitosamente'})

@main_routes.route('/upload_resume', methods=['POST'])
def upload_resume():
    data = request.form
    file = request.files['resumeFile']
    # Aquí guardaríamos el archivo y los detalles en la base de datos
    return jsonify({'message': 'Hoja de vida cargada con éxito'})
