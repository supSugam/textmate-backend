from dotenv import load_dotenv
import nltk
nltk.download('punkt')

load_dotenv()

from app import app

if __name__ == '__main__':
    app.run(port=5984)
