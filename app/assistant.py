from .chunking import Chunk
from .retrieval import retrieve


def answer_question(question: str, chunks: list[Chunk], top_k: int = 4) -> dict:
    matches = retrieve(question, chunks, top_k=top_k)
    if not matches or matches[0][1] < 0.15:
        return {
            "answer": "I could not find sufficient supporting information in the indexed documents.",
            "grounded": False,
            "citations": [],
        }

    citations = []
    sentences = []
    for chunk, score in matches:
        excerpt = chunk.text[:320].strip()
        citations.append({
            "document_id": chunk.document_id,
            "document_name": chunk.document_name,
            "chunk_id": chunk.chunk_id,
            "excerpt": excerpt,
        })
        sentences.append(f"[{len(citations)}] {excerpt}")
    answer = (
        "The indexed documents contain the following relevant evidence. "
        "This prototype returns retrieved passages rather than generating a synthesized LLM answer:\n"
        + "\n".join(sentences)
    )
    return {"answer": answer, "grounded": True, "citations": citations}
