# Gemma-powered Compliance Agent

A modular FastAPI agent for document ingestion, retrieval-augmented generation, and compliance-focused QA using Gemma models.

## 🚀 Setup


## 📦 API Endpoints
-  — Ask questions against ingested documents
-  — Upload and index PDF files

## 🧪 Testing

## 🛠 Project Structure
```
agent-training/
├── app/                  # Main FastAPI app
│   ├── main.py           # Entry point
│   ├── routes/           # API endpoints
│   ├── services/         # Business logic
│   ├── utils/            # Helpers
│   ├── models/           # Pydantic schemas
│   └── config.py         # Centralized settings
├── tests/                # Unit tests
├── data/                 # Indexed PDFs and embeddings
├── scripts/              # CLI tools
├── notebooks/            # Prototyping
├── configs/              # YAML/JSON configs
└── README.md             # Project overview
```
