"""
This script runs the FlaskWebApp application using a development server.
"""
import gunicorn
from os import environ
from FlaskWebApp import app

if __name__ == '__main__':
    
    app.run()
