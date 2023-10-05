# from app import app
from flask import request
from app import api
from http import HTTPStatus
from flask_restx import Resource
from app.controllers.users_controller import UserController
from app.schemas.users_schema import UserRequestSchema

user_ns = api.namespace(
  name='Users',
  path='/users',
  description='Rutas de usuarios'
)
schema_request = UserRequestSchema(user_ns)

@user_ns.route('')
class Roles(Resource):
  def get(self):
    '''listar todo los usuarios'''
    controller=UserController()
    return controller.fetch_all()
  
  @user_ns.expect(schema_request.create(),validate = True)
  def post(self):
    '''crear un usuario'''
    controller=UserController()
    return controller.save(request.json)

@user_ns.route('/<int:id>')
class Roles(Resource):
  def get(self,id):
    '''obtener un usuario por su id'''
    controller=UserController()
    return controller.find_by_id(id)
  
  
  # def put(self,id):
  #   return f'Actualizar rol {id}'
  def delete(self,id):
    '''Inhabilitar un usuario por su id'''
    controller=UserController()
    return controller.remove(id)
  
  @user_ns.expect(schema_request.create(),validate = True)
  def patch(self,id):
    '''actualizar un usuario por su id'''
    controller=UserController()
    return controller.update(id,request.json)



# user_ns = api.namespace(
#   name='Roles',
# )

# @role_ns.route('')
# class Roles(Resource):
#   def get(self):
#     pass


# @app.route('/roles', methods=['GET'])
# def list_roles():
#   return 'Listado de roles'

# @app.route('/roles', methods=['POST'])
# def create_roles():
#   return 'creacion de roles'

# @app.route('/role/<int:id>', methods=['PUT', 'PATCH'])
# def update_roles(id):
#   return f'Actualizar rol {id}'

# @app.route('/role/<int:id>', methods=['DELETE'])
# def delete_roles(id):
#   return f'eliminando rol {id}'