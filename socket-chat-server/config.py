from decouple import config


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = config('MY_SECRET_KEY', default="my_secret_key")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True