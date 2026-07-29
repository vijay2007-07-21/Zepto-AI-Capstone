from pathlib import Path

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_PATH = BASE_DIR / "docs"
CHROMA_DB_PATH = BASE_DIR / "chroma_db"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ChromaDB collection
COLLECTION_NAME = "zepto_support"