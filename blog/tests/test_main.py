from fastapi import FastAPI,requests
from fastapi.testclient import TestClient

from blog.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "ok!"}

def test_read_main_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    # assert response.json == {"detail": "Not Found"}
