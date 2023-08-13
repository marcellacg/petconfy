from flask_cors import CORS
from helpers.database import app, db, migrate, login_manager
from models.User import User
from models.Pet import Pet
from routes.user import user
from routes.pet import pet
from routes.passeioparque import servicoUm


CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object('config')

login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)


with app.app_context():
    db.create_all()
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.register_blueprint(user, url_prefix='/users') #user vem de routes
app.register_blueprint(pet, url_prefix='/pets')
app.register_blueprint(servicoUm, url_prefix='/passeioparque')


if __name__ == '__main__':
    app.debug = True
    app.run()