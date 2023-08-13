from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from forms.PetForms import FormularioPet
from models.User import User
from models.Pet import Pet
from flask import render_template, flash
from helpers.database import app, db


@app.route('/pet/', methods=['GET', 'POST'])
@login_required
def cadastroPet():
    form = FormularioPet()
    if form.validate_on_submit():
        user_id = current_user.id
        user = User.query.get(user_id)
        pet = Pet(nome=form.nomePet.data, idade=form.idade.data,
                  especie=form.especie.data, observacoes=form.observacoes.data, user=user)
        db.session.add(pet)
        db.session.commit()
        print("passou pela inserção")
        return redirect(url_for('home'))
    return render_template('cadastropet.html', form=form)


@app.route('/pets', methods=['GET'])
@login_required
def getPet():
    if current_user.is_authenticated:
        user_id = current_user.id
        # Listar os pets do usuário logado
        pets = Pet.query.filter_by(user_id=user_id).all()
        return render_template('pets.html', pets=pets)


@app.route('/pets/<int:id>', methods=['GET', 'DELETE'])
@login_required
def deletePet(id):
    if current_user.is_authenticated:
        user_id = current_user.id
        pet = Pet.query.get(id)
        if pet is not None:
            db.session.delete(pet)
            db.session.commit()
            pets = Pet.query.filter_by(user_id=user_id).all()
            return render_template('pets.html', pets=pets)
        else:
            return 'PET NÃO ENCONTRADO'
    else:
        return 'SEM AUTORIZAÇÃO', 405


@app.route('/pets/<int:id>', methods=['GET', 'POST'])
@login_required
def updatePet(id):
    if current_user.is_authenticated:
        user_id = current_user.id
    else:
        return None
    pet = Pet.query.get(id)
    if not pet:
        flash('PET NÃO ENCONTRADO', 'error')
        return redirect(url_for('pets'))

    if pet.user_id != user_id:
        flash('PERMISSÃO NEGADA', 'error')
        return redirect(url_for('pets'))

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        especie = request.form['especie']
        observacoes = request.form['observacoes']
        pet.nome = nome
        pet.idade = idade
        pet.especie = especie
        pet.observacoes = observacoes
        db.session.commit()

    pets = Pet.query.filter_by(user_id=user_id).all()
    return render_template('pets.html', pets=pets)