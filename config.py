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

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY='testkeyindevconfig'
    DEBUG = True

class TestConfig(Config):
    SECRET_KEY='testkeyintestconfig'

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}              