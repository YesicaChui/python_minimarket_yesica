from app import db
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token
from http import HTTPStatus

class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel

    def sign_in(self, body):
        try:
            username = body['username']
            record = self.model.where(username=username,status=True).first()
            if record:
                password = body['password']
                if record.check_password(password):
                    user_id = record.id
                    access_token = create_access_token (identity= user_id)
                    return {
                        'access_token':access_token
                    },HTTPStatus.OK
                return {
                    'message':f'La contraseña es incorrecta'
                }, HTTPStatus.UNAUTHORIZED
            
            return {
                'message':f'No se encontro el usuario: {username}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return{
                'message':'Ocurrio un error',
                'error':str(e)
            },HTTPStatus.INTERNAL_SERVER_ERROR