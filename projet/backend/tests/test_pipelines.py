def test_get_pipelines_empty(client):
    resp = client.get("/pipelines/1")
    assert resp.status_code == 200
    assert resp.json() == []


def test_sync_pipelines_no_token(client):
    resp = client.post("/pipelines/1/sync")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
