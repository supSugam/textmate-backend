# app/gpt.py
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_response(file_content):
    # Add your logic here to generate a response using GPT-3.5
    # For simplicity, let's assume the summarized text is the same as the input text
    summarized_text = file_content

    # For demonstration purposes, let's split the text into sentences
    sentences = [sentence.strip() for sentence in summarized_text.split('.') if sentence]

    return summarized_text, sentences
