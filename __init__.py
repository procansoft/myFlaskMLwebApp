"""
The flask application package.
"""
import gunicorn
from flask import Flask
app = Flask(__name__)

import FlaskWebApp.views
