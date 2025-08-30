# Development Setup

This guide will help you set up the MKZenith development environment.

## Prerequisites

- Python 3.9 or higher
- Git
- Poetry (for dependency management)
- Node.js and npm (for documentation)
- Docker and Docker Compose (optional)

## Getting Started

### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/your-username/MKZenith.git
cd MKZenith

# Add the upstream repository
git remote add upstream https://github.com/MKWorldWide/MKZenith.git
```

### 2. Set Up Python Environment

We use Poetry for dependency management. Install it if you haven't already:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Configure Poetry to create virtual environments in the project directory
poetry config virtualenvs.in-project true

# Install dependencies
poetry install --with dev

# Activate the virtual environment
poetry shell
```

### 3. Install Pre-commit Hooks

```bash
pre-commit install
```

### 4. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your configuration
# (See Configuration section below)
```

## Configuration

Create a `.env` file with the following variables:

```env
# Application
ENVIRONMENT=development
LOG_LEVEL=DEBUG

# Google Cloud
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
GOOGLE_DRIVE_FOLDER_ID=your-folder-id

# Gemini AI
GEMINI_API_KEY=your-gemini-api-key
```

## Development Workflow

### Running the Application

```bash
# Start the development server
uvicorn mkzenith.app:app --reload

# Or using the CLI
mkzenith run
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=mkzenith --cov-report=html

# Run a specific test file
pytest tests/test_module.py

# Run a specific test function
pytest tests/test_module.py::test_function_name
```

### Linting and Formatting

```bash
# Run all linters and formatters
pre-commit run --all-files

# Or run individually
black .
isort .
flake8
mypy .
bandit -r mkzenith
```

### Documentation

```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Code Style

We follow the following code style guidelines:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **mypy** for static type checking
- **Google-style** docstrings

## Git Workflow

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

2. Make your changes and commit them with a descriptive message:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   # or
   git commit -m "fix: fix bug in module"
   ```

3. Push your changes to your fork:
   ```bash
   git push origin your-branch-name
   ```

4. Create a pull request against the `main` branch.

## Testing

We use `pytest` for testing. Follow these guidelines:

- Write tests for all new features and bug fixes
- Keep tests simple and focused
- Use fixtures for common test data
- Aim for high test coverage

## Documentation

We use MkDocs with the Material theme for documentation. Follow these guidelines:

- Keep documentation up-to-date with code changes
- Use clear and concise language
- Add examples for complex features
- Document all public APIs

## Code Review Process

1. Create a pull request with your changes
2. Ensure all tests pass and code coverage remains high
3. Request a review from at least one maintainer
4. Address any feedback or requested changes
5. Once approved, a maintainer will merge your changes

## Release Process

1. Update the version number in `pyproject.toml`
2. Update the `CHANGELOG.md` with the changes
3. Create a release on GitHub
4. The CI/CD pipeline will automatically publish the package to PyPI

## Troubleshooting

### Common Issues

#### Missing Dependencies

```bash
# Install missing dependencies
poetry install
```

#### Test Failures

```bash
# Run tests with more verbose output
pytest -v

# Run tests with debugging
pytest --pdb
```

#### Linting/Formatting Issues

```bash
# Auto-fix formatting issues
black .
isort .

# Fix simple linting issues automatically
autopep8 --in-place --recursive .
```

### Getting Help

If you encounter any issues, please:
1. Check the [troubleshooting guide](../troubleshooting.md)
2. Search the [GitHub issues](https://github.com/MKWorldWide/MKZenith/issues)
3. Open a [new issue](https://github.com/MKWorldWide/MKZenith/issues/new) if your problem isn't documented
