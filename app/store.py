from dataclasses import dataclass, field
from .chunking import Chunk


@dataclass
class Document:
    document_id: str
    filename: str
    chunks: list[Chunk]


@dataclass
class InMemoryStore:
    documents: dict[str, Document] = field(default_factory=dict)

    def add(self, document: Document) -> None:
        self.documents[document.document_id] = document

    def all_chunks(self) -> list[Chunk]:
        return [chunk for doc in self.documents.values() for chunk in doc.chunks]

    def delete(self, document_id: str) -> bool:
        return self.documents.pop(document_id, None) is not None
