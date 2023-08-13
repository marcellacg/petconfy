from flask import Blueprint
from controllers.PetController import cadastroPet, getPet, deletePet, updatePet

pet = Blueprint('pet', __name__)

pet.route('/pet', methods=['GET', 'POST'])(cadastroPet)
pet.route('/pets', methods=['GET'])(getPet)
pet.route('/pets/<int:id>', methods=['GET', 'DELETE'])(deletePet)
pet.route('/pets/<int:id>', methods=['GET', 'POST'])(updatePet)