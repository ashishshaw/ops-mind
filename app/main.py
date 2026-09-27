from fastapi import FastAPI
from pydantic import BaseModel

from app.services.chat import ChatService


app = FastAPI(
    title="OpsMind",
    description="AI-Powered Engineering Knowledge & Operations Assistant",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.post("/api/chat")
async def chat(request: ChatRequest):
    service = ChatService()

    answer = await service.ask(request.message)

    return {
        "answer": answer,
    }
