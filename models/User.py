from helpers.database import db
from flask_login import UserMixin
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(150), unique=True)
    endereco = db.Column(db.String())
    senha_hash = db.Column(db.String())
    entrada_em = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    # pets = db.relationship('Pet', backref='pets', lazy=True)

    def __init__(self, nome, email, endereco, senha_hash):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.senha_hash = senha_hash

    def __repr__(self) -> str:
        return "<User nome={}>".format(self.nome)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)