from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    from .routes import main
    app.register_blueprint(main)

    return app 