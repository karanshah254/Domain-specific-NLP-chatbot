# 🎓 VGEC Intelligent AI Assistant

An AI-powered domain-specific NLP chatbot developed for **Vishwakarma Government Engineering College (VGEC), Ahmedabad**.  
The system provides automated conversational support for admissions, courses, fees, placements, and other college-related queries.

---

## 🚀 Project Overview

This project implements a **Natural Language Processing (NLP) based chatbot** capable of:

- Understanding user queries using text preprocessing
- Performing intent classification using Machine Learning
- Providing domain-restricted responses
- Serving responses through a FastAPI backend

The chatbot is specifically designed to answer queries related to:
- Admissions
- Eligibility
- Courses offered
- Fee structure
- Hostel & facilities
- Placements
- Contact & location details

---

## 🧠 Technical Architecture

User Input  
⬇  
FastAPI Backend  
⬇  
NLP Preprocessing  
⬇  
TF-IDF Vectorization (n-grams)  
⬇  
Logistic Regression Classifier  
⬇  
Intent Prediction  
⬇  
Response Engine  

---

## 🛠 Tech Stack

- **Backend:** FastAPI
- **NLP:** NLTK
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Vectorization:** TF-IDF (Unigrams + Bigrams)
- **Language:** Python
- **Deployment Ready:** Uvicorn

---

## 📂 Project Structure

```
NLP_PROJECT/
├── app.py                      # FastAPI application & routes
├── model.py                    # NLP preprocessing & ML classifier
├── intents.json                # Intent dataset (20+ intents)
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── __pycache__/                # Python cache directory
└── documentation/              # Additional documentation
    ├── backend.md              # Backend API documentation
    ├── model_trained_step4.md  # Model training & step documentation
    ├── NLP_PIPELINE.md         # NLP pipeline architecture
    └── overview.md             # Project overview & specifications
```


---

## 📊 Features

- 20+ domain-specific intents
- 200+ training patterns
- Domain restriction logic (prevents unrelated responses)
- Vocabulary-based fallback mechanism
- REST API integration
- Swagger UI testing support

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/karanshah254/Domain-specific-NLP-chatbot
cd Domain-specific-NLP-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run FastAPI Server

```bash
uvicorn app:app --reload
```

### 4️⃣ Open API Docs (Swagger UI)

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example API Request

Send the following JSON in the `/chat` endpoint:

```json
{
  "message": "What is the fee structure at VGEC?"
}
```

Example Response:

```json
{
  "response": "Undergraduate tuition is around ₹6,000 total..."
}
```

---

## 🎯 Future Enhancements

- Replace TF-IDF with transformer-based embeddings (BERT)
- Integrate MongoDB for dynamic knowledge retrieval
- Develop Angular-based frontend chat interface
- Deploy on cloud platforms (Render / AWS)
- Add multilingual support (English, Hindi, Gujarati)
- Implement confidence scoring visualization
- Add user session context handling

---

## 👨‍💻 Author

Karan Shah  
AI/ML & Full Stack Developer  

---

## 📌 Academic Value

This project demonstrates:

- Applied NLP pipeline design
- Intent classification using Machine Learning
- Domain-restricted conversational AI system
- Backend API development with FastAPI
- Real-world system architecture implementation
- Practical integration of NLP theory with production-ready software

---


<!-- REPO DESCRIPTION -->
<!-- An AI-powered domain-specific NLP chatbot for Vishwakarma Government Engineering College (VGEC), built using FastAPI, TF-IDF vectorization, and Logistic Regression for intelligent intent classification and domain-restricted conversational assistance. -->