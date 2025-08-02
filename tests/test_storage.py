from pathlib import Path

from storage import DailyEntry, save_entry


def test_save_entry(tmp_path: Path):
    entry = DailyEntry(
        "mind",
        "heart",
        "energy",
        "intention",
        "hi",
        "positive",
    )
    file_path = save_entry(entry, directory=tmp_path)
    assert file_path.exists()
    content = file_path.read_text()
    assert "Mindset" in content
