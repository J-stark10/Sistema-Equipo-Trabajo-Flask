from flask import Flask
from flask_migrate import Migrate
from src.extensions import db, bcrypt, login_manager
from src.models import User

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("src.config.Config")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # importacion de bp
    from src.main.routes import main_bp
    from src.auth.routes import auth_bp
    from src.miembros.routes import bp_miembro
    from src.tareas.routes import bp_tarea

    # resgistrar el bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(bp_miembro, url_prefix='/miembros')
    app.register_blueprint(bp_tarea, url_prefix='/tareas')

    with app.app_context():
        db.create_all()

    return app