"""
Importing modules

OS (Operating System): for creating directories
Flask: for backend routes, configuration and app creation
Blueprint: For organising flask application into modular components.
Request: For handling HTTP requests
Jsonify: For cconverting python dictionaries into a JSON response
Pipeline: From the hugging face library, creates an end-to-end pipeline.
"""

from flask import Blueprint, request, jsonify
from transformers import pipeline

summarise_bp = Blueprint('summarise', __name__) # Creating a new blueprint, for handling routes to text summarisation.

summariser = pipeline("summarization") # Uses a pre-trained model from Hugging Face to intialise a summarisation pipeline.

@summarise_bp.route('/summarise', methods=['POST']) # Route decorator, for summarisation.

# Function that is called when a POST request by the user is mode to the "/summarise" route.

def summarise_text():
    data = request.get_json() # Retrieve JSON data set in POST request.
    text = data.get('text', '') # Extract the value associated with the text key.

    if not text: # If the text is empty, display error.
        return jsonify({'error': 'No text provided'}), 400

    # Run the summariser pipeline, defining default arguments and then return summary.
    summary = summariser(text, max_length=100, min_length=25, do_sample=False)[0]['summary_text']
    return jsonify({'summary' : summary})