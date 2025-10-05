from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "username": "johndoe777",
            "email": "johndoe777@gmail.com",
            "password": "Johndoe777@",
            "role": "staff"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["success"] is True
    assert data["data"]["username"] == "johndoe777"
    assert data["data"]["email"] == "johndoe777@gmail.com"
    assert data["data"]["role"] == "staff"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert isinstance(data["data"], list)
    if data["data"]:
        user = data["data"][0]
        assert "id" in user
        assert "username" in user
        assert "email" in user
        assert "role" in user
        assert "created_at" in user
        assert "updated_at" in user


def test_read_single_user():
    users_response = client.get("/users/").json()
    if users_response["data"]:
        user_id = users_response["data"][0]["id"]
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"]["id"] == user_id

def test_update_user():
    users_response = client.get("/users/").json()
    if users_response["data"]:
        user_id = users_response["data"][0]["id"]
        response = client.put(
            f"/users/{user_id}",
            json={
                "username": "johndoe_updated",
                "email": "johndoe_updated@gmail.com",
                "password": "Johndoe1@",
                "role": "admin"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["data"]["username"] == "johndoe_updated"
        assert data["data"]["email"] == "johndoe_updated@gmail.com"
        assert data["data"]["role"] == "admin"

def test_delete_user():
    users_response = client.get("/users/").json()
    if users_response["data"]:
        user_id = users_response["data"][0]["id"]
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        check_response = client.get(f"/users/{user_id}")
        assert check_response.status_code == 404