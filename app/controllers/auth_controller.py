from os import getenv
from app import db,mail
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from http import HTTPStatus
from secrets import token_hex
from flask_mail import Message

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
                    refresh_token = create_refresh_token (identity= user_id)
                    return {
                        'access_token':access_token,
                        'refresh_token':refresh_token
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
        
    def refresh_token(self,identity):
        try:
            access_token = create_access_token(identity=identity)
            return {
                'access_token':access_token
            }, HTTPStatus.OK
        except Exception as e:
            return{
                'message': 'Ocurrio un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def password_reset(self, body):
        try:
            email = body['email']
            record = self.model.where(email=email, status=True).first()
            if record:
                new_password = token_hex(6)
                record.password =new_password
                record.hash_password()

                self.db.session.add(record)
                self.db.session.commit()
                message = Message(
                    subject=f'Reinicio de contraseña - {email}',
                    sender=('Flask Boilerplate',getenv('MAIL_USERNEME')),
                    recipients=[email],
                    # body=f'Esta es tu nueva contraseña: {new_password}'
                    html=f'<h1 style="color:blue;text-align:center">Esta es tu nueva contraseña</h1><h2 style="background-color:yellow;text-align:center">{new_password}</h2> '
                )
                mail.send(message)

                return{
                    # 'message': f'la contraseña nueva es {new_password}'
                    'message': f'la contraseña nueva es {new_password}'
                },HTTPStatus.OK
            return {
                'message':f'No se encontro el usuario con el correo : {email}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return{
                'message': 'Ocurrio un error',
                'error':str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()
