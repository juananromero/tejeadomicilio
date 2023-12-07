from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME='databaseteje.sqlite'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Product
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """Si uso sqlite, debo crear el fichero de la base de datos.
    Con MySQL, por ejemplo, este paso sería crear la bdd en el servidor.
    Al llamar a db.create_all() crea la bdd si no existe y añade las
    tablas si no existen en el dir 'instance'. Si existen, no hace nada."""
    DATABASE=path.join(app.instance_path, DB_NAME)
    with app.app_context():
        db.create_all()
    
