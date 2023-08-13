from flask import Blueprint
from controllers.UserController import index, register, login, home, protected, logout, perfil, agenda, admin, procurar

user = Blueprint('user', __name__)

user.route('/', methods=['GET'])(index)
user.route('/home', methods=['GET'])(home)
user.route('/register', methods=['POST', 'GET'])(register)
user.route('/login', methods=['GET', 'POST'])(login)
user.route('/protected', methods=['GET', 'POST'])(protected)
user.route('/logout')(logout)
user.route('/perfil')(perfil)
user.route('/agenda')(agenda)
user.route('/admin')(admin)
user.route('/admin/search', methods=['GET'])(procurar)
# user.route('/<int:user_id>/edit', methods=['POST'])(update)
# user.route('/<int:user_id>', methods=['DELETE'])(delete)