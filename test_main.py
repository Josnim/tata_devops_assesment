from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_devops_post_success():
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "token-de-prueba"
    }
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from_user": "Rita Astoria",
        "timeToLifeSec": 45
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_devops_invalid_api_key():
    headers = {"X-Parse-REST-API-Key": "clave-falsa", "X-JWT-KWY": "test"}
    payload = {
        "message": "test",
        "to": "test",
        "from_user": "test",
        "timeToLifeSec": 1
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    assert response.status_code == 403