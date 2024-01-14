from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

def train_classifier(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train a Support Vector Machine (SVM) classifier
    classifier = SVC(kernel='linear', C=1.0, random_state=42)
    classifier.fit(X_train_tfidf, y_train)

    # Evaluate the classifier
    predictions = classifier.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    return classifier, vectorizer, accuracy, report

def classify_text(text, classifier, vectorizer):
    # Vectorize the input text using TF-IDF
    text_tfidf = vectorizer.transform([text])

    # Classify the text using the trained classifier
    classification_result = classifier.predict(text_tfidf)[0]

    return classification_result
