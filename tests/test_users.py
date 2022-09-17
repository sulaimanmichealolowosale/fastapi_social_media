from fastapi.testclient import TestClient
from app import schemas
from app.main import app
from app.schemas import *


client = TestClient(app)


def test_root():
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == "hello world"
    assert res.status_code == 200


def test_create_user():
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "sulaiman"})
    new_user = schemas.GetUser(**res.json())
    assert res.status_code == 201
    assert new_user.email == "hello123@gmail.com"
