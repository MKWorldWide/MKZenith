"""Audio transcription utilities using Google Speech-to-Text."""

from __future__ import annotations

import logging
from pathlib import Path

try:
    from google.cloud import speech_v1 as speech
except Exception:  # pragma: no cover - handled in tests
    speech = None

logger = logging.getLogger(__name__)


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe an audio file using Google Speech-to-Text."""
    if speech is None:
        raise RuntimeError("google-cloud-speech is not installed")

    if not audio_path.is_file():
        logger.warning("Audio file missing: %s", audio_path)
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    try:
        client = speech.SpeechClient()
        with audio_path.open("rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code="en-US",
        )
        response = client.recognize(config=config, audio=audio)
        transcript = " ".join(
            result.alternatives[0].transcript for result in response.results
        )
        logger.info("Transcription succeeded for %s", audio_path)
        return transcript
    except Exception as exc:  # pragma: no cover - network errors
        logger.exception("Transcription failed for %s: %s", audio_path, exc)
        raise
