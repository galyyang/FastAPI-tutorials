from fastapi import FastAPI,requests
from fastapi.testclient import TestClient

from blog.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["message"] == "Hello!"


def test_read_main_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    # assert response.json == {"detail": "Not Found"}
