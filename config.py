import os

class Config:
    '''
    General configuration parent class
    '''
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SECRET_KEY = 'youwillneverknowmysecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moses:123456@localhost/blogposts'



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}