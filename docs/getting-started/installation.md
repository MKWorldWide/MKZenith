# Installation

This guide will help you set up MKZenith on your local machine for development and testing purposes.

## Prerequisites

- Python 3.9 or higher
- Git
- Google Cloud Platform account with:
  - Speech-to-Text API enabled
  - Drive API enabled
  - Service account with appropriate permissions
- Google Gemini API key

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/MKWorldWide/MKZenith.git
cd MKZenith
```

### 2. Set Up a Virtual Environment

We recommend using a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install the package in development mode with all dependencies
pip install -e '.[dev]'
```

### 4. Set Up Environment Variables

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

   # Application Settings
   LOG_LEVEL=INFO
   ENVIRONMENT=development
   ```

### 5. Set Up Pre-commit Hooks

We use pre-commit hooks to ensure code quality. Install them with:

```bash
pre-commit install
```

## Verifying the Installation

To verify that everything is set up correctly, run the test suite:

```bash
pytest
```

## Development Dependencies

For development, you might want to install additional tools:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Or install specific tools
pip install black isort flake8 mypy bandit safety pre-commit
```

## Docker (Optional)

If you prefer using Docker, you can build and run the application with:

```bash
# Build the Docker image
docker build -t mkzenith .

# Run the container
docker run -p 8000:8000 --env-file .env mkzenith
```

## Troubleshooting

### Common Issues

1. **Missing Dependencies**: Ensure all dependencies are installed with `pip install -r requirements.txt`
2. **Environment Variables**: Verify that all required environment variables are set in your `.env` file
3. **Google Cloud Authentication**: Make sure your Google Cloud credentials are properly set up
4. **Port Conflicts**: If port 8000 is in use, change it in the `.env` file or with the `PORT` environment variable

### Getting Help

If you encounter any issues, please:
1. Check the [troubleshooting guide](troubleshooting.md)
2. Search the [GitHub issues](https://github.com/MKWorldWide/MKZenith/issues)
3. Open a [new issue](https://github.com/MKWorldWide/MKZenith/issues/new) if your problem isn't documented
