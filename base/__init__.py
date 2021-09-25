from api import api
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api.bp)

    return app
