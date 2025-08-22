from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ask import router as ask_router
from app.routes.ingest import router as ingest_router  # 👈 NEW
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Gemma-powered Compliance Agent",
    description="Modular RAG agent for compliance QA using Gemma and FAISS",
    version="0.1.0"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(ask_router, prefix="/ask", tags=["Ask"])
app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])  # 👈 NEW

# Root HTML response
@app.get("/", response_class=HTMLResponse)
async def root():
    logger.info("Root endpoint accessed")
    return "<h2>✅ Gemma-powered Compliance Agent is Running</h2>"

# Health check
@app.get("/health")
async def health():
    logger.info("Health check passed")
    return {"status": "ok"}

# Version info
@app.get("/version")
async def version():
    return {"version": app.version}
