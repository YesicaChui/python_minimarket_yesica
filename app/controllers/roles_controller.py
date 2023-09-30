from app import db
from app.models.roles_models import RoleModel
from app.schemas.roles_schema import RoleResponseSchema
from http import HTTPStatus
class RolesController:
  def __init__(self):
    self.db =db
    self.model = RoleModel
    self.schema = RoleResponseSchema

  def fetch_all(self):
    records = self.model.all()
    response = self.schema(many=True)   
    return response.dump(records)
  
  def save(self,body):
    try:
        record_new = self.model.create(**body)
        self.db.session.add(record_new)
        self.db.session.commit()
        return {
          'creacion de rol', HTTPStatus.CREATED
          }
    except Exception as e:
      self.db.session.rollback()
      return {
        'message': 'Ocurrio un error',
        'error':str(e)
      }, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
      self.db.session.close()

  
    