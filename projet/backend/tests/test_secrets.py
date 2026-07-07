def test_get_secrets_no_token(client):
    resp = client.get("/secrets/1")
    assert resp.status_code == 400
    assert "token" in resp.json()["detail"].lower()
