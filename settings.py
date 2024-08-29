import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SHORT_ID_REGEXP = os.getenv('SHORT_ID_REGEXP')
