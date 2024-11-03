# NLTK API

A Flask-based REST API that provides common Natural Language Processing operations using NLTK.

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Health Check

- **URL:** `/health`
- **Method:** `GET`
- **Response:** `{"status": "healthy"}`

### 2. Text Tokenization

- **URL:** `/api/tokenize`
- **Method:** `POST`
- **Body:**

```json
{
  "text": "Your text here."
}
```

- **Response:**

```json
{
  "word_tokens": ["Your", "text", "here", "."],
  "sentence_tokens": ["Your text here."]
}
```

### 3. Part of Speech (POS) Tagging

- **URL:** `/api/pos-tag`
- **Method:** `POST`
- **Body:**

```json
{
  "text": "Your text here."
}
```

- **Response:**

```json
{
  "pos_tags": [
    { "word": "Your", "tag": "PRP$" },
    { "word": "text", "tag": "NN" },
    { "word": "here", "tag": "RB" },
    { "word": ".", "tag": "." }
  ]
}
```

### 4. Named Entity Recognition (NER)

- **URL:** `/api/ner`
- **Method:** `POST`
- **Body:**

```json
{
  "text": "John works at Google in New York."
}
```

- **Response:**

```json
{
  "named_entities": [
    { "text": "John", "type": "PERSON" },
    { "text": "Google", "type": "ORGANIZATION" },
    { "text": "New York", "type": "GPE" }
  ]
}
```

### 5. Sentiment Analysis

- **URL:** `/api/sentiment`
- **Method:** `POST`
- **Body:**

```json
{
  "text": "Your text here."
}
```

- **Response:**

```json
{
  "sentiment": {
    "neg": 0.0,
    "neu": 1.0,
    "pos": 0.0,
    "compound": 0.0
  }
}
```

## Error Handling

All endpoints return appropriate error messages with corresponding HTTP status codes when:

- No text is provided
- An internal error occurs

## Example Usage (Python)

```python
import requests
import json

url = "http://localhost:5000/api/tokenize"
data = {"text": "Hello, this is a test sentence!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.json())
```
