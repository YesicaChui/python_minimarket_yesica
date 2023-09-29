# from app import app
from app import api
from http import HTTPStatus
from flask_restx import Resource
from app.controllers.roles_controller import RolesController

role_ns = api.namespace(
  name='Roles',
  path='/roles',
  description='Rutas de roles'
)

@role_ns.route('')
class Roles(Resource):
  def get(self):
    '''Listado de roles'''
    controller = RolesController()
    return controller.all()
  def post(self):
    '''Creacion de roles'''
    return 'creacion de roles'

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


