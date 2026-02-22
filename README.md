# 🎓 VGEC Intelligent AI Assistant

An AI-powered domain-specific NLP chatbot developed for **Vishwakarma Government Engineering College (VGEC), Ahmedabad, Gujarat, India**.

This project implements a full-stack conversational AI system using **FastAPI (Python)** for backend NLP processing and **Angular** for a professional frontend chat interface.

---

## 🚀 Project Overview

VGEC Intelligent AI Assistant is designed to provide automated responses to student queries related to:

- Admissions
- Eligibility
- Courses Offered
- Fee Structure
- Placements
- Hostel & Facilities
- Contact & Location
- Scholarships
- Faculty Information

The chatbot uses Machine Learning for **intent classification** and ensures responses are strictly restricted to the VGEC domain.

---

## 🧠 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INPUT                               │
│                    (Student Query Text)                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   FRONTEND LAYER                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │   Angular Chat UI (domain-specific-chat-ui/)              │  │
│  │   • Material Design Components                            │  │
│  │   • Chat Component (chat.component.ts)                    │  │
│  │   • Chat Service (chat.service.ts)                        │  │
│  │   • HTTP Client for API Communication                     │  │
│  │   • localStorage for Chat Persistence                     │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP POST Request
                             │ /chat endpoint
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   BACKEND API LAYER                              │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │   FastAPI Server (app.py)                                 │  │
│  │   • REST API Endpoint: /chat                              │  │
│  │   • CORS Middleware                                       │  │
│  │   • Request/Response Handling                             │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  NLP PROCESSING LAYER                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │   Model Pipeline (model.py)                               │  │
│  │                                                            │  │
│  │   1. Text Preprocessing (NLTK)                            │  │
│  │      • Tokenization                                       │  │
│  │      • Lowercasing                                        │  │
│  │      • Stopword Removal                                   │  │
│  │      • Lemmatization                                      │  │
│  │                                                            │  │
│  │   2. Feature Extraction                                   │  │
│  │      • TF-IDF Vectorization                               │  │
│  │      • N-gram Range: (1,2) - Unigrams + Bigrams           │  │
│  │                                                            │  │
│  │   3. Intent Classification                                │  │
│  │      • Logistic Regression Model                          │  │
│  │      • class_weight='balanced'                            │  │
│  │      • Trained on intents.json                            │  │
│  │                                                            │  │
│  │   4. Domain Validation                                    │  │
│  │      • Vocabulary-based Restriction                       │  │
│  │      • VGEC-specific Intent Matching                      │  │
│  │                                                            │  │
│  │   5. Response Generation                                  │  │
│  │      • Intent-to-Response Mapping                         │  │
│  │      • Random Selection from Response Pool                │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │   Training Data (intents.json)                            │  │
│  │   • 20+ Domain-Specific Intents                           │  │
│  │   • 200+ Training Patterns                                │  │
│  │   • Intent-Response Mappings                              │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   RESPONSE DELIVERY                              │
│  • JSON Response to Frontend                                    │
│  • Typing Animation Effect                                      │
│  • Auto-scroll to Latest Message                                │
│  • Chat History Persistence                                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠 Tech Stack

### 🔹 Backend
- Python
- FastAPI
- NLTK
- Scikit-learn
- TF-IDF Vectorizer (ngram_range=(1,2))
- Logistic Regression (class_weight='balanced')

### 🔹 Frontend
- Angular (Standalone Component Architecture)
- Angular Material
- HttpClientModule
- CSS Animations
- localStorage for chat persistence

---

## 📂 Project Structure

```
NLP_PROJECT/
│
├── app.py                          # FastAPI backend server
├── model.py                        # NLP model training and prediction logic
├── intents.json                    # Training data with intents and patterns
├── requirements.txt                # Python dependencies
├── README.md
│
├── __pycache__/                    # Python cache files
│
├── documentation/
│   ├── backend.md
│   ├── model_trained_step4.md
│   ├── NLP_PIPELINE.md
│   └── overview.md
│
└── domain-specific-chat-ui/        # Angular frontend application
    ├── angular.json
    ├── package.json
    ├── server.ts
    ├── tsconfig.json
    ├── tsconfig.app.json
    ├── tsconfig.spec.json
    └── src/
        ├── index.html
        ├── main.ts
        ├── main.server.ts
        ├── styles.css
        ├── app/
        │   ├── app.component.ts
        │   ├── app.component.html
        │   ├── app.component.css
        │   ├── app.config.ts
        │   ├── app.routes.ts
        │   ├── chat/
        │   │   ├── chat.component.ts
        │   │   ├── chat.component.html
        │   │   └── chat.component.css
        │   └── services/
        │       ├── chat.service.ts
        │       └── chat.service.spec.ts
        └── assets/
```

---

## ✨ Features Implemented

### 🤖 Intelligent NLP Engine
- 20+ domain-specific intents
- 200+ training patterns
- Text preprocessing (tokenization, stopword removal, lemmatization)
- TF-IDF vectorization with bigrams
- Logistic Regression classifier
- Vocabulary-based domain restriction

---

### 🌐 REST API Backend
- `/chat` endpoint
- CORS enabled for Angular integration
- Swagger UI testing support

---

### 💬 Professional Angular Chat UI
- Angular Material design
- User & Bot message separation
- Animated typing indicator
- Smooth message fade-in animation
- Auto-scroll to latest message
- Disabled send button during loading
- HTML-rendered bot responses
- Clickable official VGEC website link

---

### 🎨 Advanced UI Enhancements
- Watermark-style VGEC logo inside chatbox
- Transparent background logo (non-intrusive)
- Fully scrollable chat area
- Professional toolbar branding
- Responsive layout

---

### 💾 Chat Persistence
- Chat history stored in localStorage
- Chat remains after page refresh
- Welcome message shown only on first load

---

## ▶️ How to Run

### 🔹 Backend Setup

1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Run FastAPI server

```bash
uvicorn app:app --reload
```

3️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

### 🔹 Frontend Setup

1️⃣ Navigate to Angular frontend folder

```bash
cd domain-specific-chat-ui
```

2️⃣ Install dependencies

```bash
npm install
```

3️⃣ Add Angular Material (if not already added)

```bash
ng add @angular/material
```

4️⃣ Run Angular development server

```bash
ng serve
```

Or if you want to run the server-side rendering:

```bash
node server.ts
```

5️⃣ Open in browser

```
http://localhost:4200
```

---

## 🧪 Example API Request (http://127.0.0.1:8000/docs)

```json
{
  "message": "What is the fee structure at VGEC?"
}
```

Example Response:

```json
{
  "response": "Undergraduate tuition is around ₹6,000 total. For more information, visit: Official VGEC Website"
}
```

---

## 🔐 Domain Restriction Logic

The chatbot:
- Validates vocabulary match
- Restricts responses to VGEC-related queries
- Returns fallback message for unrelated topics

Example:

Input: `Virat Kohli`
Response:
"Sorry, I can only answer questions related to Vishwakarma Government Engineering College."

---

## 🎯 Academic Significance

This project demonstrates:

- Applied Natural Language Processing pipeline design
- Intent classification using supervised learning
- Backend API development
- Full-stack system integration
- Conversational AI architecture
- User experience design principles
- Real-world domain-restricted chatbot implementation

---

## 👨‍💻 Author

Karan Shah (Final-Year-Student at VGEC, 2022-26)<br>
AI/ML & Full Stack Developer

---

## 🏫 Institution

Vishwakarma Government Engineering College
Ahmedabad, Gujarat, India<br>
Official Website: https://vgecg.ac.in/

---

## 📌 License

This project is developed for academic and demonstration purposes.

---