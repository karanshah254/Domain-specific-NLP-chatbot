### STEP 4 — TRAIN INTENT CLASSIFIER

This step trains an intent classifier on the TF-IDF vectors created earlier. A Logistic Regression model is fit on `X` (vectorized sentences) and `all_labels` (intent names), giving the system a probabilistic classifier for intent detection.

After training, the pipeline runs a quick sanity print to confirm the model is trained, then uses a prediction helper that:
- Preprocesses the incoming sentence and vectorizes it with the same `TfidfVectorizer`.
- Computes intent probabilities with `predict_proba`.
- Applies a confidence threshold (0.45) to decide whether to return a fallback message or a best-match intent.

This makes the chatbot robust to out-of-domain inputs while still returning high-confidence intent responses for known patterns.
