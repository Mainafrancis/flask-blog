from flask import Flask
from config import configurations
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import configure_uploads,IMAGES,UploadSet
