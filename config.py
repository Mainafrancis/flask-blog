import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTES_URL = 'https://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        