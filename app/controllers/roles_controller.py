from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RoleResponseSchema
from http import HTTPStatus
class RolesController:
  def __init__(self):
    self.db =db
    self.model = RoleModel
    self.schema = RoleResponseSchema

  def fetch_all(self):
    records = self.model.where(status=True).all()
    response = self.schema(many=True)   
    return response.dump(records)
  
  def save(self,body):
    try:
        record_new = self.model.create(**body)
        self.db.session.add(record_new)
        self.db.session.commit()
        return { 'message': f'El rol {body["name"]} se ha creado',}, HTTPStatus.CREATED
          
    except Exception as e:
      self.db.session.rollback()
      return {
        'message': 'Ocurrio un error',
        'error':str(e)
      }, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
      self.db.session.close()

  def find_by_id(self, id):
    try:
      record =self.model.where(id=id,status=True).first()

      if record:
        response =self.schema(many=False)
        return response.dump(record)
      return {
        'message':f'no encontrado'
      }, HTTPStatus.NOT_FOUND

    
      
    except Exception as e:
       return {
        'message': 'Ocurrio un error',
        'error':str(e)
      }, HTTPStatus.INTERNAL_SERVER_ERROR

  def update(self, id, body):
     try:
         record =self.model.where(id=id,status=True).first()
         if record:
            record.update(**body)
            self.db.session.add(record)
            self.db.session.commit()
            return {
              'mensaje': f'el rol con el id: {id} ha sido actualizado'
            }, HTTPStatus.OK 
         return {
            'message':f'no encontrado'
          }, HTTPStatus.NOT_FOUND        
     except Exception as e:
        self.db.session.rollback()
        return {
          'message': 'Ocurrio un error',
          'error':str(e)
        }, HTTPStatus.INTERNAL_SERVER_ERROR
     finally:
        self.db.session.close()

  def remove(self,id):
     try:
         record =self.model.where(id=id,status=True).first()
         if record:
            record.update(status=False)
            self.db.session.add(record)
            self.db.session.commit()
            return {
              'mensaje': f'el rol con el id: {id} ha sido inhabilitado'
            }, HTTPStatus.OK 
         return {
            'message':f'no encontrado'
          }, HTTPStatus.NOT_FOUND        
     except Exception as e:
        self.db.session.rollback()
        return {
          'message': 'Ocurrio un error',
          'error':str(e)
        }, HTTPStatus.INTERNAL_SERVER_ERROR
     finally:
        self.db.session.close()
    