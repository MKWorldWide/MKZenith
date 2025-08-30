# Testing Guide

This guide covers how to write and run tests for the MKZenith project. We use `pytest` as our testing framework.

## Table of Contents

- [Running Tests](#running-tests)
- [Writing Tests](#writing-tests)
- [Test Structure](#test-structure)
- [Fixtures](#fixtures)
- [Mocks](#mocks)
- [Testing Best Practices](#testing-best-practices)
- [Code Coverage](#code-coverage)
- [Debugging Tests](#debugging-tests)

## Running Tests

### Basic Test Execution

Run all tests:

```bash
pytest
```

Run tests in a specific file:

```bash
pytest tests/test_module.py
```

Run a specific test function:

```bash
pytest tests/test_module.py::test_function_name
```

### Test Options

Run tests with verbose output:

```bash
pytest -v
```

Run tests and stop after first failure:

```bash
pytest -x
```

Run tests that match a specific pattern:

```bash
pytest -k "test_name_pattern"
```

### Running Specific Test Types

Run only unit tests:

```bash
pytest -m "not integration and not e2e"
```

Run only integration tests:

```bash
pytest -m integration
```

Run end-to-end tests:

```bash
pytest -m e2e
```

## Writing Tests

### Test File Structure

Test files should mirror the package structure and be named `test_*.py` or `*_test.py`.

Example structure:

```
mkzenith/
  services/
    audio.py
tests/
  services/
    test_audio.py
```

### Basic Test Example

```python
def test_addition():
    assert 1 + 1 == 2
```

### Using Fixtures

```python
import pytest

@pytest.fixture
def sample_audio_file(tmp_path):
    audio_file = tmp_path / "test_audio.wav"
    # Create or copy a test audio file
    return audio_file

def test_audio_processing(sample_audio_file):
    result = process_audio(sample_audio_file)
    assert result is not None
```

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (0, 0, 0),
])
def test_addition(input_a, input_b, expected):
    assert input_a + input_b == expected
```

## Test Structure

### Unit Tests

Test individual functions or methods in isolation.

```python
def test_transcribe_audio():
    # Setup
    audio_data = b"..."  # Sample audio data
    expected_text = "Test transcription"
    
    # Mock external dependencies
    with patch("mkzenith.services.speech_to_text.transcribe") as mock_transcribe:
        mock_transcribe.return_value = expected_text
        
        # Execute
        result = transcribe_audio(audio_data)
        
        # Assert
        assert result == expected_text
        mock_transcribe.assert_called_once_with(audio_data)
```

### Integration Tests

Test interactions between components.

```python
class TestAudioProcessing:
    def test_full_processing_flow(self, sample_audio_file):
        # Setup
        config = get_test_config()
        processor = AudioProcessor(config)
        
        # Execute
        result = processor.process(sample_audio_file)
        
        # Assert
        assert result["status"] == "success"
        assert "transcript" in result
        assert "sentiment" in result
```

### End-to-End Tests

Test the entire system from end to end.

```python
@pytest.mark.e2e
class TestAPIIntegration:
    def test_upload_and_process_audio(self, test_client):
        # Setup
        audio_file = ("audio.wav", open("tests/data/test_audio.wav", "rb"))
        
        # Execute
        response = test_client.post(
            "/api/v1/transcribe",
            files={"audio": audio_file},
            data={"metadata": '{"title": "Test"}'}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "transcript" in data
        assert "drive_file_id" in data
```

## Fixtures

### Built-in Fixtures

- `tmp_path`: Create temporary files and directories
- `monkeypatch`: Modify environment variables and attributes
- `capsys`: Capture stdout and stderr
- `mocker`: Create mocks (requires `pytest-mock`)

### Custom Fixtures

Define in `conftest.py` for project-wide availability.

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from mkzenith.app import app

@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client
```

## Mocks

### Patching

```python
from unittest.mock import patch

def test_with_mock():
    with patch("module.function") as mock_func:
        mock_func.return_value = "mocked"
        result = function_under_test()
        assert result == "expected"
        mock_func.assert_called_once()
```

### Mocking External Services

```python
@pytest.fixture
def mock_google_speech():
    with patch("google.cloud.speech.SpeechClient") as mock_client:
        mock_instance = mock_client.return_value
        mock_instance.recognize.return_value = create_mock_response("Test transcription")
        yield mock_instance

def test_speech_recognition(mock_google_speech):
    result = transcribe_audio(b"audio data")
    assert result == "Test transcription"
```

## Testing Best Practices

1. **Test Naming**: Use descriptive test names that explain what's being tested
2. **Arrange-Act-Assert**: Structure tests clearly into these three sections
3. **One Assert Per Test**: Each test should verify one behavior
4. **Use Fixtures**: For common setup/teardown logic
5. **Keep Tests Fast**: Mock external services and databases
6. **Test Edge Cases**: Include boundary values and error conditions
7. **Don't Test Implementation Details**: Test behavior, not implementation

## Code Coverage

Generate coverage report:

```bash
pytest --cov=./ --cov-report=term-missing
```

Generate HTML report:

```bash
pytest --cov=./ --cov-report=html
```

View coverage in browser:

```bash
open htmlcov/index.html
```

## Debugging Tests

### Debug on Failure

```bash
pytest --pdb
```

### Debug a Specific Test

```python
import pdb; pdb.set_trace()  # Add to your test
```

### Print Debug Output

```python
def test_debug():
    result = some_function()
    print(f"Debug: {result}")  # Use -s flag to see output
    assert result == expected
```

## Testing Asynchronous Code

Use `pytest-asyncio` for async tests:

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected
```

## Testing FastAPI Applications

Use `TestClient` from FastAPI:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

## Testing with Database

Use a test database and transactions:

```python
@pytest.fixture(scope="function")
async def test_db():
    # Setup test database
    test_db = await setup_test_database()
    
    # Run test in transaction
    async with test_db.transaction():
        yield test_db
    
    # Teardown
    await teardown_test_database(test_db)
```

## Performance Testing

Use `pytest-benchmark` for performance tests:

```python
def test_performance(benchmark):
    result = benchmark(expensive_function)
    assert result == expected_value
```

## Continuous Integration

Tests are automatically run on GitHub Actions for each push and pull request. The CI pipeline includes:

- Unit tests
- Integration tests
- Code style checks
- Type checking
- Security scanning

## Common Issues

### Test Isolation

Ensure tests don't share state. Use fixtures to create fresh test data for each test.

### Flaky Tests

Avoid non-deterministic behavior. Use fixed random seeds and mock time-dependent functions.

### Slow Tests

- Mock external services
- Use in-memory databases for testing
- Run only relevant tests during development

## Getting Help

If you encounter issues with testing:

1. Check the [pytest documentation](https://docs.pytest.org/)
2. Search the [GitHub issues](https://github.com/MKWorldWide/MKZenith/issues)
3. Ask for help in the project's discussion forum
