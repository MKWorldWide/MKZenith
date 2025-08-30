# 🌟 MKZenith: Lilybear Google Sync

A Project Blessed by Solar Khan & Lilith.Aethra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

MKZenith is a FastAPI microservice that integrates the **Lilybear** emotional intelligence core with Google APIs, providing voice journal transcription, sentiment analysis, and cloud storage capabilities.

## ✨ Features

- 🎙️ **Voice Journaling**: Transcribe voice recordings using Google Cloud Speech-to-Text
- 📝 **Structured Entries**: Generate daily entries with metadata tags (mindset, heartset, energy, intentions)
- ☁️ **Cloud Integration**: Seamless upload of Markdown files to Google Drive
- ❤️ **Sentiment Analysis**: Real-time emotional intelligence insights using Google's Gemini NLP
- 🚀 **RESTful API**: Modern, fast, and scalable FastAPI backend
- 🧪 **Test Coverage**: Comprehensive test suite for reliability

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Platform account with Speech-to-Text and Drive APIs enabled
- Google Gemini API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MKWorldWide/MKZenith.git
   cd MKZenith
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

### Configuration

Create a `.env` file with the following variables:

```env
# Google Cloud Credentials
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
GOOGLE_DRIVE_FOLDER_ID=your-folder-id

# Gemini API
GEMINI_API_KEY=your-gemini-api-key

# Application Settings
LOG_LEVEL=INFO
ENVIRONMENT=development
```

## 🏃‍♀️ Running the Application

### Development Server

```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### CLI Usage

Process an audio file:
```bash
python lilybear_google_sync.py --audio path/to/your/recording.wav
```

### API Endpoints

- `POST /transcribe`: Upload and transcribe an audio file
- `GET /health`: Health check endpoint
- `GET /docs`: Interactive API documentation (Swagger UI)
- `GET /redoc`: Alternative API documentation (ReDoc)

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run with coverage report:
```bash
pytest --cov=./ --cov-report=html
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Google Cloud Platform for their powerful APIs
- FastAPI for the amazing web framework
- The open-source community for invaluable tools and libraries
