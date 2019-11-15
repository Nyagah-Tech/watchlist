# from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap

# #Initializing application 
# app = Flask(__name__,instance_relative_config = True)

# #setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# #initializing flask extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error

from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
def create_app(config_name):

    app = Flask(__name__) 
    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    #will add the views forms

    return app

    