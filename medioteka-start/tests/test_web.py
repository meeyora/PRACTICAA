import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

@pytest.mark.parametrize("url", ["/", "/lab", "/privacy", "/login", "/video/1"])
def test_pages_open(client, url):
    assert client.get(url).status_code == 200

def test_unknown_video_returns_404(client):
    assert client.get("/video/9999").status_code == 404

def test_training_form(client):
    assert client.post("/login", data={"username":"student-demo", "password":"practice-only"}).status_code == 200
