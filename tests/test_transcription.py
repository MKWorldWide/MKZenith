import types
from pathlib import Path

import transcription
from transcription import transcribe_audio


class DummySpeech:
    class RecognitionConfig:
        class AudioEncoding:
            LINEAR16 = 1

        def __init__(self, **kwargs):
            pass

    class RecognitionAudio:
        def __init__(self, content):
            self.content = content

    class SpeechClient:
        def recognize(self, config, audio):
            return types.SimpleNamespace(
                results=[
                    types.SimpleNamespace(
                        alternatives=[
                            types.SimpleNamespace(transcript="hello world")
                        ]
                    )
                ]
            )


def test_transcribe_audio(monkeypatch, tmp_path: Path):
    audio_file = tmp_path / "test.wav"
    audio_file.write_bytes(b"fake")
    monkeypatch.setattr(transcription, "speech", DummySpeech)
    text = transcribe_audio(audio_file)
    assert text == "hello world"
