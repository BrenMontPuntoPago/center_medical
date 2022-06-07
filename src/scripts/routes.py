from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

banca.add_url_rule(
<<<<<<< HEAD
    '/doctor', view_func=controllers.doctor, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/paciente', view_func=controllers.listaFuntionPaciente, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/diagnostico', view_func=controllers.listaFuntionDiagnostico, methods=['GET,POST,PUT'])

=======
    '/doctor', view_func=controllers.cruDoctor, methods=['GET', 'POST', 'PUT'])

# banca.add_url_rule(
#     '/paciente', view_func=controllers.paciente, methods=['GET,POST,PUT'])
# banca.add_url_rule(
#     '/diagnostico', view_func=controllers.diagnostico, methods=['GET,POST,PUT'])
>>>>>>> 3b6fed489ad402a610b9f47512649727c218291a


