from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, template_folder='/home/marcella/Documentos/petconfy/templates')
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
