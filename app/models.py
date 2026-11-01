from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)
    top_k: int = Field(default=4, ge=1, le=10)


class Citation(BaseModel):
    document_id: str
    document_name: str
    chunk_id: str
    excerpt: str


class AskResponse(BaseModel):
    answer: str
    grounded: bool
    citations: list[Citation]
