from fastapi import FastAPI
from app.graph import get_answer
from app.models import QueryRequest, QueryResponse

app = FastAPI(
    title="Zepto AI Support Assistant",
    description="Offline RAG Support Assistant using LangGraph + ChromaDB",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Zepto AI Support Assistant is running!"
    }


@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):
    result = get_answer(request.query)

    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"],
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )