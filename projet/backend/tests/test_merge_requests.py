def test_get_merge_requests_empty(client):
    resp = client.get("/merge-requests/1")
    assert resp.status_code == 200
    assert resp.json() == []


def test_sync_merge_requests_no_token(client):
    resp = client.post("/merge-requests/1/sync")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
