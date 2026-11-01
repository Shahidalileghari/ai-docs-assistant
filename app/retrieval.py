import re
from collections import Counter
from .chunking import Chunk


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def retrieve(question: str, chunks: list[Chunk], top_k: int = 4) -> list[tuple[Chunk, float]]:
    query = Counter(tokenize(question))
    if not query:
        return []
    ranked = []
    for chunk in chunks:
        terms = Counter(tokenize(chunk.text))
        overlap = sum(min(count, terms[token]) for token, count in query.items())
        # Simple transparent baseline; production retrieval should combine lexical
        # search, semantic embeddings, metadata filters, and reranking.
        score = overlap / max(sum(query.values()), 1)
        if score > 0:
            ranked.append((chunk, score))
    return sorted(ranked, key=lambda item: (-item[1], item[0].ordinal))[:top_k]
