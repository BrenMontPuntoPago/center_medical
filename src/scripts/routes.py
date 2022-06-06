from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)


banca.add_url_rule(
    '/doctor', view_func=controllers.doctor, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/paciente', view_func=controllers.paciente, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/diagnostico', view_func=controllers.diagnostico, methods=['GET,POST,PUT'])



