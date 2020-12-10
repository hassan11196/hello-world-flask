import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = 'SOME_RANDOM_KEY'
    TEMPLATES_AUTO_RELOAD = True
    