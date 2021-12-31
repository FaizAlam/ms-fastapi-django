from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_home():
    response = client.get("/") #request.get("")
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']

def test_post_home():
    response = client.post("/") #request.get("")
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']

