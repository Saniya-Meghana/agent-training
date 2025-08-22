# routes/ask.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.gemma_agent import generate_response

router = APIRouter()

class AskRequest(BaseModel):
    query: str

@router.get("/")
async def health_check():
    return {"status": "Ask route is live!"}

@router.post("/query")
async def ask_agent(request: AskRequest):
    response = generate_response(request.query)
    return {"query": request.query, "response": response}
