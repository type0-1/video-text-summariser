"""
Importing modules

OS (Operating System): for creating directories
Flask: for backend routes, configuration and app creation
Blueprint: For organising flask application into modular components.
Request: For handling HTTP requests
Jsonify: For converting python dictionaries into a JSON response
Secure_Filename: For secure handling of filenames.
"""

import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

# Creating a new blueprint. __name__ is used for Flask to locate the blueprint.

upload_bp = Blueprint('upload', __name__)
upload_folder = 'uploads' # Defining the uploads directory where uploaded files will be saved.

os.makedirs(upload_folder, exist_ok=True) # Created directory specified in upload_folder if not created.

@upload_bp.route('/upload', methods=['POST']) # Route decorator for the upload functionality 

# Function to handle upload functionality
def upload_video():
    if 'video' not in request.files: # Check if video is in the request module files.
        return jsonify({'error': 'No video file has been provided!'}) # Error message
    
    video = request.files['video'] # Store uploaded vile in video
    filename = secure_filename(video.filename) # Sanitising filename (Make sure the filename is safe for use)
    video_path = os.path.join(upload_folder, filename) # Construct the full path by combining "upload_folder" path and sanitised filename.
    video.save(video.path) # This is to save the video to the specified path


    # Initialise and display success message. 
    
    success_message = jsonify({'message': 'Video has been uploaded successfully', 'video_path': video_path})

    return success_message
