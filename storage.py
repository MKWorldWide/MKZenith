"""Local storage utilities for journal entries."""

from __future__ import annotations

import datetime
from dataclasses import dataclass
from pathlib import Path

from config import ENTRIES_DIR


@dataclass
class DailyEntry:
    mindset: str
    heartset: str
    energy: str
    intentions: str
    transcript: str | None = None
    sentiment: str | None = None

    def to_markdown(self) -> str:
        return (
            f"# {datetime.date.today()}\n\n"
            f"- \U0001F9E0 Mindset: {self.mindset}\n"
            f"- \U0001FA60 Heartset: {self.heartset}\n"
            f"- \U0001F321\uFE0F Energy: {self.energy}\n"
            f"- \U0001F3AF Intentions: {self.intentions}\n"
            + (
                f"\n**Transcript**:\n{self.transcript}\n"
                if self.transcript
                else ""
            )
            + (
                f"\n**Sentiment**: {self.sentiment}\n"
                if self.sentiment
                else ""
            )
        )


def save_entry(entry: DailyEntry, directory: Path = ENTRIES_DIR) -> Path:
    """Persist an entry to markdown."""
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / f"{datetime.date.today()}.md"
    file_path.write_text(entry.to_markdown())
    return file_path
