def test_get_repository_not_found(client):
    resp = client.get("/repository/1")
    assert resp.status_code == 404


def test_sync_repository_no_token(client):
    resp = client.post("/repository/1/sync")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
