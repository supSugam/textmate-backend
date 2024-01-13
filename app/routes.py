from flask import render_template, request, jsonify
from .gpt import generate_response

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    try:
        data = request.get_json()
        file_content = data.get('file_content', '')

        # Call the function to generate a response using GPT-3.5
        summarized_text, sentences = generate_response(file_content)

        return jsonify({
            'summarized_text': summarized_text,
            'sentences': sentences,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
