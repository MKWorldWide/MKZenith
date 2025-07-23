# Lilybear Google Sync

This repository contains a minimal prototype for integrating the
**Lilybear** emotional intelligence core with Google APIs.

## Features

- Transcribe voice journals using **Google Cloud Speech‑to‑Text**.
- Generate daily entries tagged with mindset, heartset, energy and intentions.
- Upload the generated Markdown files to Google Drive.
- Placeholder sentiment analysis using Gemini NLP.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Obtain Google OAuth credentials and place `credentials.json` in the
   repository root.
3. Run the script with an optional audio file:
   ```bash
   python lilybear_google_sync.py --audio path/to/audio.wav
   ```

The script creates a Markdown file in the `entries` directory and uploads
it to your Google Drive.
