# API Reference

This document provides detailed information about the MKZenith API endpoints, request/response formats, and authentication.

## Base URL

All API endpoints are relative to the base URL:

```
http://localhost:8000/api/v1
```

## Authentication

MKZenith uses API keys for authentication. Include your API key in the `X-API-Key` header for all requests.

```http
GET /api/v1/health
X-API-Key: your-api-key-here
```

## Response Format

All API responses are in JSON format and include the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Indicates if the request was successful |
| `data` | object | Response data (if any) |
| `error` | string | Error message (if any) |
| `timestamp` | string | ISO 8601 timestamp of the response |

## Endpoints

### Health Check

#### GET /health

Check if the API is running.

**Response:**

```json
{
  "success": true,
  "data": {
    "status": "OK",
    "version": "1.0.0",
    "environment": "development"
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

### Authentication

#### POST /auth/token

Get an access token.

**Request Body:**

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 3600
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

### Audio Processing

#### POST /transcribe

Transcribe an audio file and save to Google Drive.

**Request Headers:**

```
Content-Type: multipart/form-data
X-API-Key: your-api-key-here
```

**Request Body (form-data):**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `audio` | file | Yes | Audio file to transcribe (WAV, MP3, FLAC) |
| `metadata` | string | No | JSON string with additional metadata |

Example metadata:

```json
{
  "title": "Morning Journal Entry",
  "tags": ["morning", "reflection"],
  "language_code": "en-US"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "transcript": "This is the transcribed text from the audio file...",
    "sentiment": {
      "score": 0.85,
      "magnitude": 0.9,
      "label": "POSITIVE"
    },
    "drive_file_id": "1A2B3C4D5E6F7G8H9I0J",
    "drive_file_url": "https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9I0J/view"
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

### Journal Entries

#### GET /entries

List all journal entries.

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | integer | No | Number of entries to return (default: 10) |
| `offset` | integer | No | Number of entries to skip (default: 0) |
| `start_date` | string | No | Filter entries after this date (ISO 8601) |
| `end_date` | string | No | Filter entries before this date (ISO 8601) |
| `tags` | string | No | Comma-separated list of tags to filter by |

**Response:**

```json
{
  "success": true,
  "data": {
    "entries": [
      {
        "id": "entry_123",
        "title": "Morning Journal Entry",
        "content": "This is the transcribed text...",
        "audio_url": "https://storage.googleapis.com/.../recording.wav",
        "drive_file_id": "1A2B3C4D5E6F7G8H9I0J",
        "sentiment": {
          "score": 0.85,
          "magnitude": 0.9,
          "label": "POSITIVE"
        },
        "tags": ["morning", "reflection"],
        "created_at": "2025-08-29T09:00:00Z",
        "updated_at": "2025-08-29T09:05:00Z"
      }
    ],
    "pagination": {
      "total": 42,
      "limit": 10,
      "offset": 0
    }
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

#### GET /entries/{entry_id}

Get a specific journal entry.

**Path Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entry_id` | string | Yes | ID of the entry to retrieve |

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "entry_123",
    "title": "Morning Journal Entry",
    "content": "This is the transcribed text...",
    "audio_url": "https://storage.googleapis.com/.../recording.wav",
    "drive_file_id": "1A2B3C4D5E6F7G8H9I0J",
    "sentiment": {
      "score": 0.85,
      "magnitude": 0.9,
      "label": "POSITIVE"
    },
    "tags": ["morning", "reflection"],
    "created_at": "2025-08-29T09:00:00Z",
    "updated_at": "2025-08-29T09:05:00Z"
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

## Error Handling

### Error Responses

All error responses follow this format:

```json
{
  "success": false,
  "error": {
    "code": "error_code",
    "message": "Human-readable error message",
    "details": {
      "field_name": "Additional error details"
    }
  },
  "timestamp": "2025-08-29T22:45:00Z"
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `invalid_request` | 400 | The request is missing required parameters or contains invalid values |
| `unauthorized` | 401 | Authentication failed or user doesn't have permissions |
| `not_found` | 404 | The requested resource was not found |
| `rate_limit_exceeded` | 429 | Too many requests, please try again later |
| `internal_error` | 500 | An internal server error occurred |

## Rate Limiting

API requests are rate limited to 1000 requests per hour per API key. The following headers are included in all responses:

- `X-RateLimit-Limit`: The maximum number of requests allowed in the current period
- `X-RateLimit-Remaining`: The number of requests remaining in the current period
- `X-RateLimit-Reset`: The time at which the current rate limit window resets (UTC epoch seconds)

## Webhooks

MKZenith can send webhook notifications for various events. To set up a webhook, configure the following environment variables:

```env
WEBHOOK_URL=https://your-webhook-url.com/endpoint
WEBHOOK_SECRET=your-webhook-secret
```

### Webhook Events

#### `entry.created`

Triggered when a new journal entry is created.

**Payload:**

```json
{
  "event": "entry.created",
  "data": {
    "id": "entry_123",
    "title": "Morning Journal Entry",
    "drive_file_id": "1A2B3C4D5E6F7G8H9I0J",
    "created_at": "2025-08-29T09:00:00Z"
  },
  "timestamp": "2025-08-29T09:00:00Z"
}
```

### Webhook Security

All webhook requests include an `X-Webhook-Signature` header that you can use to verify the request came from MKZenith. The signature is a SHA-256 HMAC of the request body using your webhook secret.

Example verification in Python:

```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    hmac_digest = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, hmac_digest)
```
