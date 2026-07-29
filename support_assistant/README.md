# Zepto AI Support Assistant

An offline AI-powered customer support assistant built using **LangGraph**, **ChromaDB**, **Sentence Transformers**, and **FastAPI**.

---

## Features

- Retrieval-Augmented Generation (RAG)
- LangGraph workflow
- ChromaDB vector database
- SentenceTransformer embeddings
- FastAPI REST API
- Offline mock implementation (No API keys required)

---

## Project Structure

```
support_assistant/
│
├── app/
│   ├── config.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── prompt.py
│   ├── graph.py
│   ├── models.py
│   └── main.py
│
├── docs/
├── chroma_db/
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd support_assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
python app/main.py
```

or

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

## POST /ask

Request

```json
{
    "query": "How can I cancel my order?"
}
```

Example Response

```json
{
    "answer": "Based on the retrieved context...",
    "sources": [
        "doc_05",
        "doc_03",
        "doc_06"
    ],
    "confidence": 1.0
}
```

---

## Technologies Used

- Python
- FastAPI
- LangGraph
- ChromaDB
- Sentence Transformers
- Pydantic
- Uvicorn

---

## Docker

Build

```bash
docker build -t zepto-ai .
```

Run

```bash
docker run -p 8000:8000 zepto-ai
```

Open

```
http://localhost:8000/docs
```

---

## Author

Vijay Morla

B.Tech Computer Science Engineering

Aditya University