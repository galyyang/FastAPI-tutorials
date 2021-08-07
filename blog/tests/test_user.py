from fastapi import FastAPI,requests
from fastapi.testclient import TestClient

from blog.main import app

client = TestClient(app)


def test_read_user_id_one():
    response = client.get("/user/1")
    assert response.status_code == 200

def test_read_non_exist_user():
    response = client.get("/user/0")
    assert response.status_code == 404