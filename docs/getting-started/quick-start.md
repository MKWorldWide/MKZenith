# Quick Start

This guide will help you get up and running with MKZenith in just a few minutes.

## Prerequisites

- Python 3.9 or higher
- Google Cloud account with Speech-to-Text and Drive APIs enabled
- Google Gemini API key

## 1. Installation

### Using pip (recommended)

```bash
# Install the package
pip install mkzenith
```

### From source

```bash
# Clone the repository
git clone https://github.com/MKWorldWide/MKZenith.git
cd MKZenith

# Install in development mode
pip install -e '.[dev]'
```

## 2. Configuration

1. Create a `.env` file in your project root:

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

## 3. Running the Application

### Start the API Server

```bash
uvicorn mkzenith.app:app --reload
```

### Using the CLI

Process an audio file:

```bash
mkzenith process --audio path/to/your/recording.wav
```

### Interactive API Documentation

Once the server is running, access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 4. Your First API Request

### Transcribe Audio

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/transcribe' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'audio=@path/to/your/recording.wav;type=audio/wav' \
  -F 'metadata={"title":"My Journal Entry","tags":["personal","reflection"]};type=application/json'
```

### Check Service Health

```bash
curl http://localhost:8000/health
```

## 5. Next Steps

- Explore the [API Reference](../usage/api.md) for detailed endpoint documentation
- Learn how to [deploy to production](../deployment/production.md)
- Check out the [examples](../examples/) for common use cases
- Read the [development guide](../development/contributing.md) to contribute to the project

## Troubleshooting

### Common Issues

1. **Missing Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Authentication Errors**:
   - Verify your Google Cloud credentials
   - Ensure the service account has the correct permissions
   - Check that the Gemini API key is valid

3. **Port Already in Use**:
   ```bash
   # Find and kill the process
   lsof -i :8000
   kill -9 <PID>
   ```

### Getting Help

- Check the [troubleshooting guide](../troubleshooting.md)
- Search the [GitHub issues](https://github.com/MKWorldWide/MKZenith/issues)
- [Open a new issue](https://github.com/MKWorldWide/MKZenith/issues/new) if your problem isn't documented
