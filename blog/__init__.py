from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from . import blues
    for blue in blues.blues_list:
        app.register_blueprint(blue)

    bootstrap.init_app(app)
    return app

__all__ = ['create_app']
