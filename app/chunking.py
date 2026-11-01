from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    document_name: str
    text: str
    ordinal: int


def split_into_chunks(document_id: str, document_name: str, text: str,
                      chunk_size: int = 900, overlap: int = 120) -> list[Chunk]:
    if chunk_size < 1 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Require chunk_size > overlap >= 0")
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    chunks = []
    start = 0
    ordinal = 0
    while start < len(normalized):
        end = min(start + chunk_size, len(normalized))
        if end < len(normalized):
            boundary = normalized.rfind(" ", start, end)
            if boundary > start + chunk_size // 2:
                end = boundary
        part = normalized[start:end].strip()
        if part:
            chunks.append(Chunk(
                chunk_id=f"{document_id}:chunk:{ordinal}",
                document_id=document_id,
                document_name=document_name,
                text=part,
                ordinal=ordinal,
            ))
            ordinal += 1
        if end >= len(normalized):
            break
        start = max(end - overlap, start + 1)
    return chunks
