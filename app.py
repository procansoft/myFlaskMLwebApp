"""
This script runs the FlaskWebApp application using a development server.
"""
import gunicorn
from os import environ
from FlaskWebApp import app

"""
The flask application package.
"""
from flask import Flask,request, jsonify, render_template
import gunicorn

import FlaskWebApp.views
app = Flask(__name__)


if __name__ == '__main__':
    
    app.run()
