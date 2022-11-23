from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST'),
    dbname=os.getenv('DBNAME')
    )
class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlitefile.db'
    DEBUG = True
