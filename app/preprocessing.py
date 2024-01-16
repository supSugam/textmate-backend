import spacy
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.lang.en.stop_words import STOP_WORDS
from .helpers import get_json_info, is_json, extract_text_from_json

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    is_json_content = is_json(text)
    summary_for_json = "The content is in JSON format"
    if is_json_content:
        json_info = get_json_info(text)
        if json_info:
            summary_for_json = f"The content is in JSON format. It includes properties like: {', '.join(json_info)}."
        # If input is JSON, extract text content
        text = extract_text_from_json(text)

    # Tokenize into sentences
    sentences = sent_tokenize(text)

    # Extract key phrases using NER (Named Entity Recognition)
    entity_relations = {}
    categories = set()
    for sentence in sentences:
        doc = nlp(sentence)

        for ent in doc.ents:
            if ent.label_ in ['PERSON', 'ORG', 'GPE']:
                # Extract relationships between entities
                if ent.text not in entity_relations:
                    entity_relations[ent.text] = set()
                for other_ent in doc.ents:
                    if ent.text != other_ent.text:
                        entity_relations[ent.text].add((other_ent.label_, other_ent.text))

        # Identify categories
        for token in doc:
            if token.pos_ == 'NOUN':
                categories.add(token.text)

    # Extract key phrases using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    feature_names = tfidf_vectorizer.get_feature_names_out()

    tfidf_phrases = []
    for i in range(tfidf_matrix.shape[0]):
        sentence_tfidf = {feature_names[j]: tfidf_matrix[i, j] for j in range(tfidf_matrix.shape[1])}
        top_word = max(sentence_tfidf, key=sentence_tfidf.get)
        tfidf_phrases.append(top_word)

    # Concatenate key phrases to form summarized text
    if is_json_content:
        summarized_text = summary_for_json
    else:
        summarized_text = generate_summary(text)

    return {
        'entity_relations': entity_relations,
        'categories': list(categories),
        'summarized_text': summarized_text,
    }


def generate_summary(text):
    # Tokenize the text
    doc = nlp(text)

    # Calculate the word frequency
    word_freq = {}
    for word in doc:
        if word.text.lower() not in STOP_WORDS:
            if word.text not in word_freq:
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # Calculate the sentence scores based on word frequency
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word.text]
                else:
                    sentence_scores[sent] += word_freq[word.text]

    # Get the most important sentences based on scores
    summarized_sentences = [sent.text for sent, score in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:3]]

    # Join the sentences to form the summary
    summarized_text = " ".join(summarized_sentences)

    return summarized_text

