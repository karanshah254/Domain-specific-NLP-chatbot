import json
import random
import re
import nltk
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# -------- 1️⃣ Download NLTK Resources (Run Once) --------
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


# -------- 2️⃣ Initialize NLP Tools --------
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


# -------- 3️⃣ Text Preprocessing Function --------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = text.split()

    cleaned_tokens = []
    for word in tokens:
        if word not in stop_words:
            lemma = lemmatizer.lemmatize(word)
            cleaned_tokens.append(lemma)

    return " ".join(cleaned_tokens)


# -------- 4️⃣ Load intents.json --------
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


all_sentences = []
all_labels = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]

    cleaned_responses = []

    for resp in intent["responses"]:
        # Remove unwanted citation patterns like :contentReference[...]
        resp = re.sub(r":contentReference\[.*?\]", "", resp)

        # Remove unwanted utm_source tracking parts inside parentheses
        resp = re.sub(r"\(.*?utm_source=.*?\)", "", resp)

        resp = resp.strip()

        # Append official website link
        resp = resp + ' For more information, visit: <a href="https://vgecg.ac.in/" target="_blank">Official VGEC Website</a>'

        cleaned_responses.append(resp)

    responses[tag] = cleaned_responses

    for pattern in intent["patterns"]:
        processed = preprocess(pattern)
        all_sentences.append(processed)
        all_labels.append(tag)


# -------- 5️⃣ Vectorization --------
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(all_sentences)


# -------- 6️⃣ Train Model --------
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X, all_labels)


# -------- 7️⃣ Chatbot Response Function --------
def chatbot_response(sentence):
    processed = preprocess(sentence)
    vector = vectorizer.transform([processed])

    # Vocabulary check
    known_words = set(vectorizer.get_feature_names_out())
    words_in_input = set(processed.split())

    common_words = words_in_input.intersection(known_words)

    # If absolutely no vocabulary match → fallback
    if len(common_words) == 0:
        return "Sorry, I can only answer questions related to Vishwakarma Government Engineering College."

    # Otherwise trust model prediction
    predicted_intent = model.predict(vector)[0]

    return random.choice(responses[predicted_intent])
