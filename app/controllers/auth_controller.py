from app import db
from app.models.users_model import UserModel
from http import HTTPStatus

class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel

    def sign_in(self, body):
        try:
            print(body)
            # record = self.model.where().first()
            return {}
        except Exception as e:
            return{
                'message':'Ocurrio un error',
                'error':str(e)
            },HTTPStatus.INTERNAL_SERVER_ERROR