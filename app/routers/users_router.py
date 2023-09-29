# from app import app
from app import api
from http import HTTPStatus
from flask_restx import Resource


role_ns = api.namespace(
  name='Users',
  path='/users'
)

@role_ns.route('')
class Roles(Resource):
  def get(self):
    return 'Listado de users'
  def post(self):
    return 'creacion de users'

@role_ns.route('/<int:id>')
class Roles(Resource):
  def get(self,id):
    return f'obtener un rol {id}'
  def put(self,id):
    return f'Actualizar rol {id}'
  def delete(self,id):
    return f'eliminando rol {id}'
  def patch(self,id):
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


