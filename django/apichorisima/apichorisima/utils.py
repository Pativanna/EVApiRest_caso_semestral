from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()

def jwt_payload_handler(user):
    return {
        'user_id': user.id,
        'email': user.correo,
        'role': user.role,
        'exp': datetime.utcnow() + timedelta(days=1),  # Token expira en 1 día
    }

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            'user_id': user.id,
            'email': user.correo,
            'role': user.role,
        }
    }

def generate_jwt_token(user):
    payload = jwt_payload_handler(user)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')

def decode_jwt_token(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

def update_last_login(sender, user, **kwargs):
    user.last_login = datetime.utcnow()
    user.save()

def create_token_for_user(user):
    token = generate_jwt_token(user)
    return token

def get_user_from_token(token):
    try:
        payload = decode_jwt_token(token)
        user_id = payload['user_id']
        return User.objects.get(id=user_id)
    except jwt.ExpiredSignatureError:
        return None  # Token ha expirado
    except jwt.InvalidTokenError:
        return None  # Token no válido

def refresh_token(token):
    user = get_user_from_token(token)
    if user:
        return create_token_for_user(user)
    return None

def obtener_rol_del_usuario(user):
    return user.role if user.is_authenticated else None
