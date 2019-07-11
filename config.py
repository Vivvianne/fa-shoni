import os

class Config:

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='qwerty'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emma:1234@localhost/fashoni'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}