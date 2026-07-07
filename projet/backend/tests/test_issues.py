def test_get_issues_empty(client):
    resp = client.get("/issues/1")
    assert resp.status_code == 200
    assert resp.json() == []


def test_sync_issues_no_token(client):
    resp = client.post("/issues/1/sync")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
