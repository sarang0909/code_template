"""
Module for functional test cases of main script.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

'''
def test_server_status():
    """Tests if server is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API server is running"}


def test_model_output():
    """Tests if model output generation api is up and giving expected result."""
    response = client.post("/model_inference/", json={"data": "test input"})
    assert response.status_code == 200
    assert response.json() == {
        "model_output": "This is dummy model output for input:test input"
    }
'''
