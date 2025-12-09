from app import create_app

def test_api_events():
    app = create_app()
    client = app.test_client()
    resp = client.get("/api/events")

    assert resp.status_code == 200
    data = resp.get_json()

    assert isinstance(data, list)
    assert {"id", "title", "date"}.issubset(data[0].keys())
