def test_get_branches_no_token(client):
    resp = client.get("/branches/1")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
