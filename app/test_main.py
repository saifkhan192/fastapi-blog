import sys

from fastapi.testclient import TestClient

from app.main import app

# sys.path.append("./app")


client = TestClient(app)


def test_get_users():
    response = client.get("/api/users")
    data = response.json()
    print(response)
    print(data)
    assert response.status_code == 200
    assert "name" in data[0]
    assert "email" in data[0]
