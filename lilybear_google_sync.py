"""CLI client for the Lilybear FastAPI service."""

from __future__ import annotations

import argparse
import requests


def main() -> None:
    parser = argparse.ArgumentParser(description="Lilybear Google Sync CLI")
    parser.add_argument("--audio", required=True, help="Path to audio file")
    parser.add_argument(
        "--api-url",
        default="http://localhost:8000",
        help="Base URL of the FastAPI service",
    )
    args = parser.parse_args()

    with open(args.audio, "rb") as audio_file:
        files = {"audio": audio_file}
        response = requests.post(f"{args.api_url}/entries", files=files)
        print(response.json())


if __name__ == "__main__":  # pragma: no cover
    main()
