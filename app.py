"""FastAPI service exposing Lilybear journal endpoints."""

from __future__ import annotations

import logging
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException

from transcription import transcribe_audio
from sentiment import analyze_sentiment
from storage import DailyEntry, save_entry
from drive import authenticate, upload_to_drive

app = FastAPI(title="Lilybear Journal Service")
logger = logging.getLogger(__name__)


@app.post("/entries")
async def create_entry(audio: UploadFile = File(...)):
    """Create a journal entry from an uploaded audio file."""
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            data = await audio.read()
            tmp.write(data)
            temp_path = Path(tmp.name)
        transcript = transcribe_audio(temp_path)
        sentiment = analyze_sentiment(transcript)
        entry = DailyEntry(
            "",
            "",
            "",
            "",
            transcript=transcript,
            sentiment=sentiment,
        )
        file_path = save_entry(entry)
        creds = authenticate()
        file_id = upload_to_drive(file_path, creds)
        return {"file_id": file_id, "sentiment": sentiment}
    except Exception as exc:  # pragma: no cover
        logger.exception("Entry creation failed: %s", exc)
        raise HTTPException(status_code=500, detail="Failed to create entry")
    finally:
        try:
            temp_path.unlink()
        except Exception:  # pragma: no cover
            pass


@app.get("/entries/{date}")
def get_entry(date: str):
    """Retrieve a stored entry by date (YYYY-MM-DD)."""
    file_path = Path(f"entries/{date}.md")
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="Entry not found")
    return file_path.read_text()
