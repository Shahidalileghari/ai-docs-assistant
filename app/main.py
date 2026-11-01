from uuid import uuid4
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
from .assistant import answer_question
from .chunking import split_into_chunks
from .models import AskRequest, AskResponse
from .store import Document, InMemoryStore

app = FastAPI(title="AI Document Assistant", version="1.0.0")
store = InMemoryStore()
ALLOWED_EXTENSIONS = {".txt", ".md"}
MAX_FILE_BYTES = 1_000_000


@app.get("/health")
def health():
    return {"status": "ok", "storage": "in-memory", "retrieval": "lexical-baseline"}


@app.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    filename = Path(file.filename or "").name
    suffix = Path(filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=415, detail="Only .txt and .md files are supported.")
    content = await file.read(MAX_FILE_BYTES + 1)
    if len(content) > MAX_FILE_BYTES:
        raise HTTPException(status_code=413, detail="File exceeds 1 MB limit.")
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded.")
    if not text.strip():
        raise HTTPException(status_code=400, detail="Document is empty.")
    document_id = str(uuid4())
    chunks = split_into_chunks(document_id, filename, text)
    store.add(Document(document_id, filename, chunks))
    return {"document_id": document_id, "filename": filename, "chunks": len(chunks)}


@app.get("/documents")
def list_documents():
    return [
        {"document_id": doc.document_id, "filename": doc.filename, "chunks": len(doc.chunks)}
        for doc in store.documents.values()
    ]


@app.delete("/documents/{document_id}")
def delete_document(document_id: str):
    if not store.delete(document_id):
        raise HTTPException(status_code=404, detail="Document not found.")
    return {"deleted": document_id}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    result = answer_question(request.question, store.all_chunks(), request.top_k)
    return result
