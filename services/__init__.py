"""
This is for registering the blueprints in:

summarise.py
upload.py
"""

# Attaining blueprints via variables

from .upload import upload_bp
from .summarise import summarise_bp

def register_blueprints(app):
    app.register_blueprint(upload_bp)
    app.register_blueprint(summarise_bp)