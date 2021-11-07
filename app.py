"""
This script runs the FlaskWebApp application using a development server.
"""
import gunicorn
from os import environ
from FlaskWebApp import app

"""
The flask application package.
"""
import gunicorn
from flask import Flask
app = Flask(__name__)

import FlaskWebApp.views


if __name__ == '__main__':
    
    app.run()
