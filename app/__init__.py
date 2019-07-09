from flask import Flask
from flask_bootstrap import Bootstrap
# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
from app.main import views