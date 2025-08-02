import pickle

import drive
from drive import authenticate


class DummyCreds:
    def __init__(self, valid=True, expired=False, refresh_token=False):
        self.valid = valid
        self.expired = expired
        self.refresh_token = refresh_token

    def refresh(self, request):  # pragma: no cover - not used in tests
        self.valid = True


def test_authenticate_uses_existing_token(tmp_path, monkeypatch):
    token = tmp_path / "token.pickle"
    creds = DummyCreds()
    token.write_bytes(pickle.dumps(creds))

    monkeypatch.setattr(drive, "build", object())
    result = authenticate(
        token_path=token,
        credentials_path=tmp_path / "creds.json",
    )
    assert isinstance(result, DummyCreds)


def test_authenticate_creates_token(tmp_path, monkeypatch):
    token = tmp_path / "token.pickle"
    creds_path = tmp_path / "creds.json"
    creds_path.write_text("{}")

    dummy_creds = DummyCreds()

    class DummyFlow:
        @classmethod
        def from_client_secrets_file(cls, *args, **kwargs):
            return cls()

        def run_local_server(self, port=0):
            return dummy_creds

    monkeypatch.setattr(drive, "build", object())
    monkeypatch.setattr(drive, "InstalledAppFlow", DummyFlow)
    monkeypatch.setattr(drive, "Request", object)

    result = authenticate(token_path=token, credentials_path=creds_path)
    assert token.exists()
    assert result is dummy_creds
