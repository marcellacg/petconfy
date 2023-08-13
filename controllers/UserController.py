import sys
from flask import render_template, redirect, url_for, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from forms.UserForms import FormularioRegistro, FormularioLogin
from models.PasseioParque import PasseioParque
from models.User import User
from flask import render_template, flash
from helpers.database import app, db

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
@login_required
def admin():
    user_id = current_user.id
    if current_user.is_authenticated and user_id == 1:
        users = User.query.all()
        return render_template('adm.html', users=users)
    else:
        return render_template('forbidden.html')

@app.route('/admin/search', methods=['GET'])
@login_required
def procurar():
    user_id = current_user.id
    if current_user.is_authenticated and user_id == 1:
        nome = request.args.get('nome')
        if nome is not None:
            users = User.query.filter(User.nome.like(f"%{nome}%")).all()
        else:
            users = User.query.all()
        return render_template('adm.html', users=users)
    else:
        return render_template('forbidden.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = FormularioRegistro()
    if form.validate_on_submit():
        user = User(nome=form.nome.data, email=form.email.data,
                    endereco=form.endereco.data, senha_hash=form.senha1.data)
        user.set_senha(form.senha1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_senha(form.senha.data):
            login_user(user)
            proximo = request.args.get("proximo")
            return redirect(proximo or url_for('home'))
        flash('Endereço de email e/ou senha inválidos.')
    return render_template('login.html', form=form)


@app.route("/forbidden", methods=['GET', 'POST'])
@login_required
def protected():
    return redirect(url_for('forbidden.html'))


@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/perfil', methods=['GET'])
@login_required
def perfil():
    if current_user.is_authenticated:
        user_id = current_user.id
        # Listar os pets do usuário logado
        perfil = PasseioParque.query.filter_by(user_id=user_id).all()
        return render_template('perfil.html', perfil=perfil)
    
@app.route('/agenda')
@login_required
def agenda():
    return render_template('agenda.html')