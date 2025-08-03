from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_create_entry_rejects_empty_audio():
    """Ensure API returns 400 for empty uploads."""
    response = client.post(
        "/entries",
        files={"audio": ("empty.wav", b"", "audio/wav")},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Empty audio file"

