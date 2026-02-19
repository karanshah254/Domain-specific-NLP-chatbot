# # ================================
# # STEP 3 — NLP PIPELINE IMPLEMENTATION
# # ================================

# # -------- IMPORT LIBRARIES --------
# import re
# import nltk
# import numpy as np

# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfVectorizer


# # -------- DOWNLOAD NLTK DATA (Run once) --------
# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("punkt_tab")
# nltk.download("wordnet")


# # -------- CREATE SAMPLE INTENT DATASET --------
# # (Temporary dataset for testing NLP pipeline)

# intents = {
#     "greeting": ["Hi", "Hello", "Good morning"],
#     "fees": [
#         "What is the tuition fee?",
#         "How much is BTech fee?",
#         "Tell me the course fees.",
#     ],
#     "admission": [
#         "How to apply?",
#         "Explain admission process",
#         "How can I get admission?",
#     ],
# }


# # -------- INITIALIZE NLP TOOLS --------
# lemmatizer = WordNetLemmatizer()
# stop_words = set(stopwords.words("english"))


# # -------- DEFINE PREPROCESSING FUNCTION --------
# def preprocess(text):
#     """
#     This function:
#     1. Converts text to lowercase
#     2. Removes punctuation
#     3. Tokenizes sentence into words
#     4. Removes stopwords
#     5. Lemmatizes words
#     """

#     text = text.lower()

#     # Remove punctuation & special characters
#     text = re.sub(r"[^a-zA-Z\s]", "", text)

#     # Tokenize into words
#     tokens = nltk.word_tokenize(text)

#     # Remove stopwords and apply lemmatization
#     cleaned_tokens = []
#     for word in tokens:
#         if word not in stop_words:
#             lemma_word = lemmatizer.lemmatize(word)
#             cleaned_tokens.append(lemma_word)

#     # Join words back into sentence
#     return " ".join(cleaned_tokens)


# # -------- APPLY PREPROCESSING TO DATASET --------
# all_sentences = []
# all_labels = []

# for intent, patterns in intents.items():
#     for sentence in patterns:
#         processed_sentence = preprocess(sentence)
#         all_sentences.append(processed_sentence)
#         all_labels.append(intent)


# # Print processed sentences
# # print("\nProcessed Sentences:")
# # for s in all_sentences:
# #     print(s)


# # -------- CONVERT TEXT TO NUMERICAL VECTORS --------
# # Using TF-IDF Vectorizer

# vectorizer = TfidfVectorizer()

# X = vectorizer.fit_transform(all_sentences)

# # print("\nTF-IDF Vector Shape:")
# # print(X.shape)


# # -------- 8️⃣ TEST WITH NEW SENTENCE --------
# test_sentence = "Tell me about BTech fees"

# processed_test = preprocess(test_sentence)
# # print("\nProcessed Test Sentence:")
# # print(processed_test)

# test_vector = vectorizer.transform([processed_test])
# # print("\nTest Vector Shape:")
# # print(test_vector.shape)


# # ================================
# # STEP 4 — TRAIN INTENT CLASSIFIER
# # ================================

# from sklearn.linear_model import LogisticRegression

# # from sklearn.model_selection import train_test_split
# # from sklearn.metrics import accuracy_score, classification_report

# # -------- Train Logistic Regression Model --------
# model = LogisticRegression()
# model.fit(X, all_labels)


# # -------- Test Model --------
# print("\nModel trained successfully on full dataset.")


# # -------- Test with New Sentences --------
# import random


# def chatbot_response(sentence):
#     processed = preprocess(sentence)
#     vector = vectorizer.transform([processed])

#     probabilities = model.predict_proba(vector)[0]
#     max_prob = max(probabilities)
#     predicted_intent = model.classes_[probabilities.argmax()]

#     CONFIDENCE_THRESHOLD = 0.45

#     # If confidence too low → fallback
#     if max_prob < CONFIDENCE_THRESHOLD:
#         return "Sorry, I can only answer questions related to university information."

#     # If confidence good → normal response
#     return random.choice(responses[predicted_intent])


# # def predict_intent(sentence):
# #     processed = preprocess(sentence)
# #     vector = vectorizer.transform([processed])
# #     prediction = model.predict(vector)
# #     return prediction[0]


# # Test examples
# # print("\nPrediction Tests:")
# # print("Input: How much is BTech fee?")
# # print("Predicted Intent:", predict_intent("How much is BTech fee?"))

# # print("\nInput: Hello there")
# # print("Predicted Intent:", predict_intent("Hello there"))

# # print("\nInput: Explain admission process")
# # print("Predicted Intent:", predict_intent("Explain admission process"))


# # ================================
# # STEP 5 — RESPONSE ENGINE
# # ================================

# responses = {
#     "greeting": [
#         "Hello! How can I help you today?",
#         "Hi there! What information do you need?",
#     ],
#     "fees": [
#         "The tuition fee is approximately ₹50,000 per year.",
#         "Fees vary depending on the course. BTech costs around ₹50,000 annually.",
#     ],
#     "admission": [
#         "You can apply online through the university admission portal.",
#         "The admission process includes filling out the form and submitting required documents.",
#     ],
# }

# print("\n🤖 Chatbot is ready! Type 'quit' to exit.\n")

# # while True:
# #     user_input = input("You: ")

# #     if user_input.lower() == "quit":
# #         print("Bot: Goodbye! 👋")
# #         break

# #     bot_reply = chatbot_response(user_input)
# #     print("Bot:", bot_reply)


# new code for model.py with actual dataset and trained model
# ================================
# model.py
# ================================

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
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')


# -------- 2️⃣ Initialize NLP Tools --------
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


# -------- 3️⃣ Text Preprocessing Function --------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
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
    responses[tag] = intent["responses"]

    for pattern in intent["patterns"]:
        processed = preprocess(pattern)
        all_sentences.append(processed)
        all_labels.append(tag)


# -------- 5️⃣ Vectorization --------
vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(all_sentences)


# -------- 6️⃣ Train Model --------
model = LogisticRegression(max_iter=1000, class_weight='balanced')
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
