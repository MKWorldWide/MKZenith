A Project Blessed by Solar Khan & Lilith.Aethra

# Lilybear Google Sync

This repository contains a prototype FastAPI microservice for integrating the
**Lilybear** emotional intelligence core with Google APIs.

## Features

- Transcribe voice journals using **Google Cloud Speech‑to‑Text**.
- Generate daily entries tagged with mindset, heartset, energy and intentions.
- Upload the generated Markdown files to Google Drive.
- Real sentiment analysis using Gemini NLP.

## Usage

1. Install dependencies and set environment variables:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   # edit .env with your Google and Gemini credentials
   ```
2. Start the FastAPI service:
   ```bash
   uvicorn app:app --reload
   ```
3. Create an entry via the CLI client:
   ```bash
   python lilybear_google_sync.py --audio path/to/audio.wav
   ```

### Running Tests

```bash
pytest
```
