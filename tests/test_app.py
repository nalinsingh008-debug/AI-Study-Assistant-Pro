from datetime import date
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_dashboard_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Study Assistant Pro" in response.text

def test_analytics_shape():
    response = client.get("/analytics")
    assert response.status_code == 200
    data = response.json()
    assert {"total_sessions", "total_hours", "total_tasks", "subject_hours"} <= data.keys()

def test_predict_endpoint():
    response = client.post("/predict", json={"study_hours": 2, "tasks_completed": 3})
    assert response.status_code == 200
    assert 0 <= response.json()["estimated_score"] <= 100

def test_invalid_predict():
    response = client.post("/predict", json={"study_hours": -1, "tasks_completed": 2})
    assert response.status_code == 422
