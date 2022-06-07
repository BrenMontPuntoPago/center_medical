from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

banca.add_url_rule(
    '/doctor', view_func=controllers.cruDoctor, methods=['GET', 'POST', 'PUT'])
banca.add_url_rule(
    '/paciente', view_func=controllers.listaFuntionPaciente, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/diagnostico', view_func=controllers.listaFuntionDiagnostico, methods=['GET,POST,PUT'])
banca.add_url_rule(
     '/especializacion', view_func=controllers.cruEspecializacion, methods=['POST,PUT'])



