### TextMate

TextMate is a small tool developed as part of a university project. It offers an abstract solution to reflect importance of scanning and analyzing lengthy documents, leveraging concepts of Natural Language Processing (NLP). By harnessing sentiment analysis and summarization techniques, TextMate aims to save time and enhance productivity in managing textual data.

### Screenshots & More Details at: [MyPortfolioWebsite/Projects/TextMate](https://sugamsubedi.com.np/projects/textmate) 🚧

#### Features 🚀
- Summarize text from .txt or .json files
- Perform sentiment analysis on text

#### Requirements 🛠️
- Flask: Backend framework for building web applications in Python.
- Flask-Cors: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- NLTK: Natural Language Toolkit for NLP tasks.
- OpenAI: Python client for the OpenAI API.
- Python-dotenv: Reads key-value pairs from a .env file and adds them to the environment.
- Scikit-learn: Machine learning library for Python.
- Spacy: An open-source NLP library for Python.

#### How to Run this Project 🏃‍♂️

**Recommended Way**:
Access the deployed version directly at [TextMate Frontend](https://textmate-frontend.vercel.app). No need to install dependencies.
(Might be down as ```pythonanywhere``` offers limited free usage)

Manual Way:
To run the textmate-backend, here are a few requirements:
- Installed Python
- Installed all libraries of requirements.txt

Step 1: Open terminal in textmate-backend folder.
Step 2: Run the command `python setup.py`

Note: This will install all the required packages of requirements.txt in your device and run the Flask app at port 5984, alternatively you can run on virtual environment using python venv.

Step 3: This should already run the flask app at port 5984 and you should be navigated to the user interface automatically.
In case you don’t, please manually visit: [TextMate Frontend](https://textmate-frontend.vercel.app)
To run the frontend code manually, you’d have to run few npm commands, but since I’ve deployed this on vercel, this is not necessary. 
