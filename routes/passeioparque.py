from flask import Blueprint
from controllers.ServicoUm import RegistroServicoUm

servicoUm = Blueprint('servicoUm', __name__)

servicoUm.route('/passeioparque', methods=['POST', 'GET'])(RegistroServicoUm)