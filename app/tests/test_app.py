from app import app

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() =={"ok" : True}

def test_place_trade():
    client = app.test_client()
    res = client.post("/trade/place", json = {"side" : "BUY"})
    data = res.get_json()
    assert res.status_code == 200
    assert data["status"] == "accepted"
    assert "id" in data

