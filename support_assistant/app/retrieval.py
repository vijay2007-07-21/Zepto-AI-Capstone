import chromadb
from sentence_transformers import SentenceTransformer

from app.config import (
    CHROMA_DB_PATH,
    EMBEDDING_MODEL,
    COLLECTION_NAME,
)

# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Connect to ChromaDB
client = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
collection = client.get_collection(COLLECTION_NAME)


def retrieve(query, top_k=3):
    """
    Retrieve the most relevant documents from ChromaDB.
    Returns documents, distances, and document IDs.
    """

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "distances"]
    )

    return {
        "documents": results["documents"][0],
        "distances": results["distances"][0],
        "ids": results["ids"][0],
    }


if __name__ == "__main__":
    question = input("Ask your question: ")

    results = retrieve(question)

    print("\nTop Results:\n")

    docs = results["documents"]
    distances = results["distances"]
    ids = results["ids"]

    for i, (doc_id, doc, distance) in enumerate(
        zip(ids, docs, distances), start=1
    ):
        print(f"Document {i}")
        print(f"ID: {doc_id}")
        print(f"Distance: {distance:.4f}")
        print("-" * 60)
        print(doc)
        print()