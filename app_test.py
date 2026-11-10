
from app import app

client = app.test_client()

def test_home():
    assert client.get("/").status_code == 200

def test_get_students():
    assert client.get("/students").status_code == 200

def test_add_student():
    res = client.post("/students", json={
        "name": "Alice",
        "course": "CS"
    })

    assert res.status_code == 201
    assert res.json["name"] == "Alice"
