from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
# Select environment based on the ENV environment variable
if os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'prod':
    print("Running in production mode")
    app.config.from_object('config.ProductionConfig')
else:
    print("Running in Github mode")
    app.config.from_object('config.GithubCIConfig')
    
db = SQLAlchemy(app)
from iebank_api.models import Account
db.create_all()
CORS(app)

from iebank_api import routes