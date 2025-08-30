# Welcome to MKZenith

![MKZenith Logo](assets/logo.png)

**MKZenith** is a powerful FastAPI microservice that integrates the **Lilybear** emotional intelligence core with Google's ecosystem, providing voice journaling, sentiment analysis, and cloud storage capabilities.

## ✨ Features

- 🎙️ **Voice Journaling**: Transcribe voice recordings using Google Cloud Speech-to-Text
- 📝 **Structured Entries**: Generate daily entries with metadata tags (mindset, heartset, energy, intentions)
- ☁️ **Cloud Integration**: Seamless upload of Markdown files to Google Drive
- ❤️ **Sentiment Analysis**: Real-time emotional intelligence insights using Google's Gemini NLP
- 🚀 **RESTful API**: Modern, fast, and scalable FastAPI backend
- 🧪 **Test Coverage**: Comprehensive test suite for reliability

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Google Cloud Platform account with Speech-to-Text and Drive APIs enabled
- Google Gemini API key

### Installation

```bash
# Clone the repository
git clone https://github.com/MKWorldWide/MKZenith.git
cd MKZenith

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e '.[dev]'

# Set up pre-commit hooks
pre-commit install
```

### Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your credentials:
   ```env
   # Google Cloud Credentials
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
   GOOGLE_DRIVE_FOLDER_ID=your-folder-id

   # Gemini API
   GEMINI_API_KEY=your-gemini-api-key
   ```

### Running the Application

Start the development server:
```bash
uvicorn app:app --reload
```

Visit the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

## 📚 Documentation

- [Getting Started](getting-started/installation.md)
- [API Reference](usage/api.md)
- [Development Guide](development/setup.md)
- [Contributing](development/contributing.md)

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guide](development/contributing.md) for details on how to submit pull requests, report issues, or suggest new features.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/MKWorldWide/MKZenith/blob/main/LICENSE.md) file for details.

## 🙏 Acknowledgments

- Google Cloud Platform for their powerful APIs
- FastAPI for the amazing web framework
- The open-source community for invaluable tools and libraries
