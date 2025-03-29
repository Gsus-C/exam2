from app.models import User, db
from flask import Blueprint, jsonify, request, redirect, url_for

routes = Blueprint('routes', __name__)

# Ruta de inicio (GET /)
@routes.route('/', methods=['GET'])
def home():
    # Página HTML sencilla con un mensaje y enlace
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Usuarios</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        h1 {
            color: #333;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        p {
            color: #555;
            font-size: 1.2rem;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1rem;
            transition: background-color 0.3s ease;
        }
        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Este es el inicio</h1>
    <a href="/users">Ver Usuarios</a>
</body>
</html>
    '''

# Ruta de login (POST /login)
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(correo=data['correo'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login exitoso', 'user': user.nombre})
    return jsonify({'message': 'Credenciales inválidas'}), 401

# Ruta para obtener listado de usuarios (GET /users)
@routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_json = [
        {'id': user.id, 'nombre': user.nombre, 'correo': user.correo, 'password': user.password}
        for user in users
    ]
    return jsonify(users_json)

# Ruta para crear usuario (POST /users)
@routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(nombre=data['nombre'], correo=data['correo'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuario creado con éxito'})