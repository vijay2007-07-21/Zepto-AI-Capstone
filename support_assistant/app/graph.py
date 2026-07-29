from typing import TypedDict, List

from langgraph.graph import StateGraph, END

from app.retrieval import retrieve


# -----------------------------
# State
# -----------------------------
class GraphState(TypedDict):
    question: str
    intent: str
    answer: str
    sources: List[str]
    confidence: float


# -----------------------------
# Intent Classification
# -----------------------------
POLICY_KEYWORDS = [
    "delivery",
    "refund",
    "return",
    "cancel",
    "membership",
    "tracking",
    "gift",
    "support",
    "payment",
    "order",
    "packed",
]


def classify_intent(state: GraphState):
    question = state["question"].lower()

    if any(word in question for word in POLICY_KEYWORDS):
        state["intent"] = "policy_question"
    else:
        state["intent"] = "general_question"

    return state


# -----------------------------
# Retrieval Node
# -----------------------------
def retrieve_and_answer(state: GraphState):
    results = retrieve(state["question"])

    docs = results["documents"]
    ids = results["ids"]

    best_doc = docs[0]

    excerpt = best_doc[:200]

    state["answer"] = (
        f"Based on the retrieved context:\n\n{excerpt}..."
    )

    state["sources"] = ids
    state["confidence"] = 1.0

    return state


# -----------------------------
# General Questions
# -----------------------------
def direct_answer(state: GraphState):
    state["answer"] = (
        "I can only answer questions about Zepto policies right now."
    )
    state["sources"] = []
    state["confidence"] = 1.0

    return state


# -----------------------------
# Router
# -----------------------------
def route_question(state: GraphState):
    return state["intent"]


# -----------------------------
# Build Graph
# -----------------------------
builder = StateGraph(GraphState)

builder.add_node("classify_intent", classify_intent)
builder.add_node("retrieve_and_answer", retrieve_and_answer)
builder.add_node("direct_answer", direct_answer)

builder.set_entry_point("classify_intent")

builder.add_conditional_edges(
    "classify_intent",
    route_question,
    {
        "policy_question": "retrieve_and_answer",
        "general_question": "direct_answer",
    },
)

builder.add_edge("retrieve_and_answer", END)
builder.add_edge("direct_answer", END)

graph = builder.compile()


# -----------------------------
# Helper Function
# -----------------------------
def get_answer(question: str):
    result = graph.invoke(
        {
            "question": question,
            "intent": "",
            "answer": "",
            "sources": [],
            "confidence": 0.0,
        }
    )

    return result


# -----------------------------
# Test
# -----------------------------
if __name__ == "__main__":
    while True:
        question = input("\nAsk your question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        result = get_answer(question)

        print("\nAnswer:")
        print(result["answer"])

        print("\nSources:")
        print(result["sources"])

        print("\nConfidence:")
        print(result["confidence"])