from flask import render_template, request, jsonify
from flask_cors import cross_origin  # Import cross_origin
from .gpt import generate_summary
from .gpt import respond_user_query

from app import app

@app.route('/')
@cross_origin()  # Enable CORS for this route
def index():
    return jsonify(message='Welcome to TextMate!')

@app.route('/summarize', methods=['POST'])
@cross_origin()  # Enable CORS for this route
def summarize_file_contents():
    try:
        data = request.get_json()
        file_content = data.get('file_content', '')

        # Call the function to generate a response using GPT-3.5
        data = generate_summary(file_content)
        return jsonify(data, 200, {'Content-Type': 'application/json; charset=utf-8'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/ask', methods=['POST'])
@cross_origin()  # Enable CORS for this route
def ask_question():
    try:
        data = request.get_json()
        file_content = data.get('file_content', '')
        question = data.get('question', '')

        # Call the function to generate a response using GPT-3.5
        answer = respond_user_query(file_content, question)
        data = {
        'answer': answer,
        }

        return jsonify(data, 200, {'Content-Type': 'application/json; charset=utf-8'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
