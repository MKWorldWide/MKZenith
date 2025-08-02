"""Google Drive integration helpers."""

from __future__ import annotations

import logging
import pickle
from pathlib import Path

try:
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    import googleapiclient.http
except Exception:  # pragma: no cover
    build = None
    InstalledAppFlow = None
    Request = None
    googleapiclient = None

from config import SCOPES, TOKEN_PATH, CREDENTIALS_PATH

logger = logging.getLogger(__name__)


def authenticate(
    token_path: Path = TOKEN_PATH,
    credentials_path: Path = CREDENTIALS_PATH,
):
    """Authenticate to Google APIs and return a credentials object."""
    if build is None:
        raise RuntimeError("google-api-python-client is not installed")

    creds = None
    if token_path.exists():
        with token_path.open("rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        try:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(credentials_path),
                    SCOPES,
                )
                creds = flow.run_local_server(port=0)
            with token_path.open("wb") as token:
                pickle.dump(creds, token)
        except Exception as exc:  # pragma: no cover
            logger.exception("Authentication failed: %s", exc)
            raise
    return creds


def upload_to_drive(file_path: Path, creds) -> str:
    """Upload a file to Google Drive and return the file ID."""
    if build is None:
        raise RuntimeError("google-api-python-client is not installed")

    if not file_path.is_file():
        logger.warning("File missing, cannot upload: %s", file_path)
        raise FileNotFoundError(file_path)

    try:
        service = build("drive", "v3", credentials=creds)
        file_metadata = {"name": file_path.name}
        media = googleapiclient.http.MediaFileUpload(
            str(file_path),
            resumable=True,
        )
        result = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        file_id = result.get("id")
        logger.info("Uploaded %s to Drive id=%s", file_path, file_id)
        return file_id
    except Exception as exc:  # pragma: no cover
        logger.exception("Drive upload failed for %s: %s", file_path, exc)
        raise
