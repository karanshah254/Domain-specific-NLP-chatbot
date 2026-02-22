from fastapi import FastAPI
from pydantic import BaseModel
from model import chatbot_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot_response(request.message)
    return {"response": response}


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Chatbot API! Send a POST request to /chat with your message."
    }
