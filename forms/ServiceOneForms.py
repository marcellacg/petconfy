
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators, DateField, TimeField
from wtforms.validators import DataRequired


class RegistroServicoUm(FlaskForm):
    data_inicial = DateField('data inicial', validators=[DataRequired('Por favor, insira a data.')], format="%Y-%m-%d")
    data_final = DateField('data final', validators=[DataRequired('Por favor, insira a data.')], format="%Y-%m-%d")

    hora_inicial = TimeField('hora inicial', validators=[DataRequired('Por favor, insira a hora.')])
    hora_final = TimeField('hora final', validators=[DataRequired('Por favor, insira a hora.')])
    
    telefone = StringField('telefone com DDD', [validators.Regexp('^[0-9]*$', message="telefone deve conter somente números"),
                            validators.Length(min=11, max=11, message="telefone deve ter no máximo 11 dígitos")])
    
    user_id = IntegerField()
    submit = SubmitField('registrar')