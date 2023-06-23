class Config():
    DEBUG = False
    STATIC = 'static'
    DATE_FORMAT = '%Y-%m-%d'
    SECRET_KEY = 'YOUR SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SERVER_NAME = 'localhost:5000'
    PREFERRED_URL_SCHEME = 'http'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:cichy@localhost/Gains_Database"
    RECAPTCHA_PUBLIC_KEY = 'YOUR RECAPTCHA PUBLIC KEY'
    RECAPTCHA_PRIVATE_KEY = 'YOUR RECAPTCHA PRIVATE KEY'
    ENV = 'development'
    DEBUG = True
