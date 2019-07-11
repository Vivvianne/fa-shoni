# import os

class Config:

    
    UPLOADED_PHOTOS_DEST ='app/static/photos'



    @staticmethod
    def init_app(app):
        pass


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://phirifo:1234@localhost/watchlist_test'

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://phirifo:1234@localhost/watchlist'
    DEBUG = True


config_options = {
'development':DevConfig
# 'production':ProdConfig,
# 'test':TestConfig
}


