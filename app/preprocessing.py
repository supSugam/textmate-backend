import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Tokenize into sentences
    sentences = sent_tokenize(text)

    # Tokenize into words and remove stop words
    stop_words = set(stopwords.words('english'))
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    filtered_sentences = [
        [word.lower() for word in sentence if word.isalnum() and word.lower() not in stop_words]
        for sentence in tokenized_sentences
    ]

    # Extract key phrases using NER (Named Entity Recognition)
    entity_phrases = []
    for sentence in sentences:
        doc = nlp(sentence)
        entities = [ent.text for ent in doc.ents if ent.label_ in ['PERSON', 'ORG', 'GPE']]
        if entities:
            entity_phrases.append(' '.join(entities))

    # Extract key phrases using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(sentence) for sentence in filtered_sentences])
    feature_names = tfidf_vectorizer.get_feature_names_out()

    tfidf_phrases = []
    for i in range(tfidf_matrix.shape[0]):
        sentence_tfidf = {feature_names[j]: tfidf_matrix[i, j] for j in range(tfidf_matrix.shape[1])}
        top_word = max(sentence_tfidf, key=sentence_tfidf.get)
        tfidf_phrases.append(top_word)

    # Concatenate key phrases to form summarized text
    summarized_text = ' '.join(entity_phrases + tfidf_phrases)

    return summarized_text
