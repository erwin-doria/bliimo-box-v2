from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config
from flask_migrate import Migrate
from instance.config import ENVIRONMENT
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[ENVIRONMENT])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)
    from .routes.home import home as home_blueprint
    from .routes.events import events as events_blueprint
    from .routes.claims import claims as claims_blueprint
    from .routes.vouchers import vouchers as vouchers_blueprint
    from .routes.response import response as response_blueprint

    from app import models

    app.register_blueprint(home_blueprint)
    app.register_blueprint(events_blueprint)
    app.register_blueprint(claims_blueprint)
    app.register_blueprint(vouchers_blueprint)
    app.register_blueprint(response_blueprint)

    return app