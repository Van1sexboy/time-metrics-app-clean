from app import app


def test_time_route_returns_json_with_unix_time():
    client = app.test_client()

    response = client.get("/time")

    assert response.status_code == 200

    data = response.get_json()

    assert "time" in data
    assert isinstance(data["time"], int)


def test_metrics_route_counts_time_requests():
    client = app.test_client()

    before_response = client.get("/metrics")
    assert before_response.status_code == 200

    before_data = before_response.get_json()
    before_count = before_data["count"]

    client.get("/time")
    client.get("/time")

    after_response = client.get("/metrics")
    assert after_response.status_code == 200

    after_data = after_response.get_json()
    after_count = after_data["count"]

    assert after_count == before_count + 2