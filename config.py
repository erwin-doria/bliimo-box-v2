class Config(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}