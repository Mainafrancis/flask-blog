from flask import Flask
from config import configurations
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import configure_uploads,IMAGES,UploadSet

app = Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(configname):
    '''
    Method for creating the app to enable for easier configurations
    '''
    app.config.from_object(configurations[configname])

    #Importing BluePrints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)