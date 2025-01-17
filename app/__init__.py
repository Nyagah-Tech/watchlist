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
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()

photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):

    app = Flask(__name__) 

   

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure uploadsset
    configure_uploads(app,photos)



    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #will add the views forms

    return app

    