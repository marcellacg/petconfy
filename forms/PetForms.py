from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, validators

class FormularioPet(FlaskForm):
    nomePet = StringField('nome', [validators.Regexp('[a-zA-Z]+', message="Nome deve conter somente letras"), validators.Length(
                                min=3, max=25, message="Nome deve ter entre 3 e 25 characteres")])
    idade = StringField('idade', [validators.Regexp('^[0-9]*$', message="idade deve conter somente números"), validators.Length(
                                min=1, max=3, message="idade deve ter no máximo 3 dígitos")])
    especie = StringField('especie', [validators.Regexp('[a-zA-Z]+', message="Espécie deve conter somente letras")])
    observacoes = StringField('observacoes (opcional)', [validators.Regexp('^[a-zA-Z0-9_.-]*$', message=""), validators.Length(
                                max=500, message="As observações devem ter no máximo 500 palavras")])
    user_id = IntegerField()
    submit = SubmitField('cadastrar')