from fastapi import FastAPI
from pydantic import BaseModel
from model import chatbot_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot_response(request.message)
    return {"response": response}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot API! Send a POST request to /chat with your message."}