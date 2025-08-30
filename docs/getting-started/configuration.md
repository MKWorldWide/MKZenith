# Configuration

MKZenith is highly configurable through environment variables. This document explains all available configuration options.

## Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to Google Cloud service account JSON key file | `/path/to/service-account.json` |
| `GOOGLE_DRIVE_FOLDER_ID` | Google Drive folder ID where files will be stored | `1A2B3C4D5E6F7G8H9I0J` |
| `GEMINI_API_KEY` | Google Gemini API key for sentiment analysis | `AIzaSyD...` |

### Optional Variables

#### Application Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `ENVIRONMENT` | `development` | Application environment: `development`, `staging`, or `production` |
| `LOG_LEVEL` | `INFO` | Logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `HOST` | `0.0.0.0` | Host to bind the application to |
| `PORT` | `8000` | Port to run the application on |
| `DEBUG` | `False` | Enable debug mode (not recommended in production) |

#### Google Cloud Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `GOOGLE_CLOUD_PROJECT` | - | Google Cloud project ID (optional if using service account) |
| `GOOGLE_DRIVE_UPLOAD_TIMEOUT` | `300` | Timeout in seconds for Google Drive uploads |
| `GOOGLE_SPEECH_LANGUAGE_CODE` | `en-US` | Language code for speech recognition |

#### Gemini AI Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `GEMINI_MODEL` | `gemini-pro` | Gemini model to use |
| `GEMINI_MAX_TOKENS` | `1024` | Maximum number of tokens to generate |
| `GEMINI_TEMPERATURE` | `0.7` | Controls randomness in generation (0.0 to 1.0) |

## Configuration File

You can also use a `.env` file in the root directory to set these variables. The file should look like this:

```env
# Application Settings
ENVIRONMENT=development
LOG_LEVEL=INFO
HOST=0.0.0.0
PORT=8000

# Google Cloud Settings
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
GOOGLE_DRIVE_FOLDER_ID=your-folder-id
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_DRIVE_UPLOAD_TIMEOUT=300
GOOGLE_SPEECH_LANGUAGE_CODE=en-US

# Gemini AI Settings
GEMINI_API_KEY=your-api-key
GEMINI_MODEL=gemini-pro
GEMINI_MAX_TOKENS=1024
GEMINI_TEMPERATURE=0.7
```

## Environment-Specific Configuration

You can create multiple environment files (e.g., `.env.development`, `.env.production`) and load them based on the `ENVIRONMENT` variable:

```bash
# Load environment-specific config
ENVIRONMENT=production uvicorn app:app
```

## Security Considerations

1. **Never commit sensitive data** to version control
2. Add `.env` to your `.gitignore` file
3. Use environment variables for production secrets
4. Restrict file permissions on service account keys

## Verifying Configuration

To verify your configuration, run:

```bash
python -c "from config import settings; print(settings)"
```

This will print the current configuration with sensitive values redacted.

## Troubleshooting

### Common Issues

1. **Missing Required Variables**: Ensure all required variables are set
2. **Incorrect File Paths**: Verify file paths in your configuration
3. **Permission Issues**: Check file permissions for service account keys
4. **Environment Not Loading**: Make sure to source your `.env` file or set variables in your environment

### Debugging

Set `LOG_LEVEL=DEBUG` to see detailed logs about configuration loading and application startup.
