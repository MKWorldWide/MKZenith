import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Default paths configurable via environment variables for flexibility
TOKEN_PATH = Path(os.getenv("TOKEN_PATH", "token.pickle"))
CREDENTIALS_PATH = Path(os.getenv("CREDENTIALS_PATH", "credentials.json"))
ENTRIES_DIR = Path(os.getenv("ENTRIES_DIR", "entries"))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# OAuth scopes for Google API access
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/documents",
]
