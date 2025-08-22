from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_query_endpoint():
    response = client.post("/ask/query", json={"query": "What is GDPR?"})
    assert response.status_code == 200
    assert "response" in response.json()
