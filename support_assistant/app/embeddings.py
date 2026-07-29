import chromadb
from sentence_transformers import SentenceTransformer

from app.config import (
    DOCS_PATH,
    CHROMA_DB_PATH,
    EMBEDDING_MODEL,
    COLLECTION_NAME,
)

model = SentenceTransformer(EMBEDDING_MODEL)

client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))

# Delete old collection if it exists
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass

collection = client.create_collection(name=COLLECTION_NAME)

documents = []
ids = []

for file in sorted(DOCS_PATH.glob("*.txt")):
    text = file.read_text(encoding="utf-8").strip()
    documents.append(text)
    ids.append(file.stem)

embeddings = model.encode(documents).tolist()

collection.add(
    ids=ids,
    embeddings=embeddings,
    documents=documents,
)

print("Documents stored successfully!")

# Verify immediately
stored = collection.get()

print("\nStored documents:")
for i, doc in enumerate(stored["documents"]):
    print(f"{stored['ids'][i]} -> {repr(doc[:80])}")