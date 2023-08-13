
from flask_login import current_user, login_required
from flask import Flask, render_template, redirect, url_for
from forms.ServiceOneForms import RegistroServicoUm
from helpers.database import db, app
from models.PasseioParque import PasseioParque
from models.User import User

@app.route('/passeioparque', methods=['POST', 'GET'])
@login_required
def passeioparque():
    form = RegistroServicoUm()
    if form.validate_on_submit():
        user_id = current_user.id
        user = User.query.get(user_id)
        passeioparque = PasseioParque(data_inicial=form.data_inicial.data, data_final=form.data_final.data,
                    hora_inicial=form.hora_inicial.data, hora_final=form.hora_final.data, telefone=form.telefone.data, user=user)
        db.session.add(passeioparque)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('servicoum.html', form=form)