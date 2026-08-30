from app import app
from fastapi.testclient import TestClient

c = TestClient(app)

def test_sum():
    r = c.post('/add-numbers', json={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json() == {"result": 5}