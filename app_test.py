from app import app

client = app.test_client()


def test_home(client):
    r = client.get("/")
    assert r.status_code == 200


def test_get_students(client):
    res = client.get("/students")  # Changed /student -> /students
    assert res.status_code == 200


def test_add_student(client):
    res = client.post("/students", json={"name": "Alice", "course": "CS"})  # Changed /student -> /students
    assert res.status_code == 201
    assert res.get_json()["name"] == "Alice"