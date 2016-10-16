import os
from flasgger import Swagger
from flask import Flask
from app.mod_api.controllers import mod_api
from app.mod_site.controllers import mod_site

app_config = {
    "development": "app.config.DevelopmentConfig",
    "default": "app.config.DevelopmentConfig"
}


def get_config_class_name():
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    return app_config[config_name]


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config_class_name())

    app.register_blueprint(mod_api)
    app.register_blueprint(mod_site)

    Swagger(app)
    return app
