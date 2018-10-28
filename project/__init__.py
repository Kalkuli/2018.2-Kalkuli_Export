import os
from flask import Flask, jsonify

# Instantiate the app
app	=	Flask(__name__)

# Set Configuration
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

from project.api.views import export_blueprint
app.register_blueprint(export_blueprint)