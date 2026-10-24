"""Customer Accounts service application factory."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///accounts.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if config:
        app.config.update(config)
    db.init_app(app)
    CORS(app)
    from service.routes import accounts
    app.register_blueprint(accounts)
    with app.app_context():
        db.create_all()
    return app
