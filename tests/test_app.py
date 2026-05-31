from app import app


def test_time_route_returns_json_with_unix_time():
    client = app.test_client()

    response = client.get("/time")

    assert response.status_code == 200

    data = response.get_json()

    assert "time" in data
    assert isinstance(data["time"], int)