from flask import Flask
from flask_cors import CORS
from app import routes
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

