"""
Importing modules

OS (Operating System): for creating directories
Flask: for backend routes, configuration and app creation
Request: For handling post/get requests
Jsonify: For creating JSON objects
Secure_Filename: For secure handling of filenames.
"""

from flask import Flask
from services import register_blueprints

# Initiating the Flask App. 
 
app = Flask(__name__) # By intialising this, the app will know where to look for content.

app.config['UPLOAD_FOLDER'] = 'uploads' # Specifies the directory that will contain uploaded files.

register_blueprints(app)

@app.route('/') # Route decorator, bound to the index page ('/')
def index(): # Returns for now, a welcome message
    return "Welcome to the video to text summarizer!"

if __name__ == "__main__":
    app.run(debug=True)