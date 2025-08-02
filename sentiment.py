"""Sentiment analysis via Gemini API."""

from __future__ import annotations

import logging

try:
    import google.generativeai as genai
except Exception:  # pragma: no cover
    genai = None

from config import GEMINI_API_KEY

logger = logging.getLogger(__name__)


class GeminiClient:
    """Thin wrapper around the Gemini generative AI API."""

    def __init__(self, api_key: str = GEMINI_API_KEY):
        if genai is None:
            raise RuntimeError("google-generativeai is not installed")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

    def analyze(self, text: str) -> str:
        prompt = (
            "Provide a one-word sentiment (positive, negative, neutral) for: "
            f"{text}"
        )
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as exc:  # pragma: no cover
            logger.exception("Gemini API failure: %s", exc)
            raise


def analyze_sentiment(text: str) -> str:
    """Convenience function for sentiment analysis."""
    client = GeminiClient()
    return client.analyze(text)
