from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    from .route import main
    app.register_blueprint(main)
    CORS(app)
    return app
