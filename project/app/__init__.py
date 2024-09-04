from flask import Flask

def setup():
    app = Flask(__name__)

    from .routes.main_routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
