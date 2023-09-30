# from app import app
from app import api
from flask import request
from http import HTTPStatus
from flask_restx import Resource
from app.controllers.roles_controller import RolesController
from app.schemas.roles_schema import RoleRequestSchema

role_ns = api.namespace(
  name='Roles',
  path='/roles',
  description='Rutas de roles'
)

schema_request = RoleRequestSchema(role_ns)

@role_ns.route('')
class Roles(Resource):
  def get(self):
    '''Listado de roles'''
    controller = RolesController()
    return controller.fetch_all()
  
  @role_ns.expect(schema_request.create(),validate = True)
  def post(self):
    '''Creacion de roles'''
    # request__json = request.json
    # if not request__json.get('name'):
    #   raise Exception('no se envio el campo name')
    # print(request.json)
    controller= RolesController()
    return controller.save(request.json)
  
  

@role_ns.route('/<int:id>')
class Roles(Resource):
  def get(self,id):
    '''obtener un rol por id'''
    return f'obtener un rol {id}'
  
  def put(self,id):
    '''Actualizar un rol por id'''
    return f'Actualizar rol {id}'
  
  def delete(self,id):
    '''eliminando un rol por id'''
    return f'eliminando rol {id}'
  
  def patch(self,id):
    '''Actualizar un rol por id'''
    return f'Actualizar rol {id}'



# role_ns = api.namespace(
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


