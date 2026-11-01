# AI Document Assistant

A production-oriented learning repository for building an AI assistant that can ingest documents, retrieve relevant evidence, answer questions with citations, and expose a secure API.

> **Learning implementation:** the included application is a deterministic, local-first RAG prototype. It demonstrates ingestion, chunking, lexical retrieval, citation assembly, API boundaries, and tests without requiring paid APIs or model credentials. It does **not** pretend to be a fully capable LLM. Provider-backed embeddings and generation are described as extension points.

## What you'll build

A document question-answering service with:
- document ingestion for `.txt` and `.md` files, plus a clear adapter design for PDF/DOCX;
- normalization, chunking, metadata, and stable source references;
- baseline lexical retrieval with ranking and relevance thresholds;
- grounded answer composition with citations and an explicit abstention path;
- FastAPI endpoints for upload, listing, deletion, and asking questions;
- input validation, file-size/type controls, path-safe storage, and basic rate-limit design;
- evaluation datasets, retrieval metrics, and regression-test strategy;
- a deployment blueprint for PostgreSQL/pgvector, object storage, background jobs, and hosted LLMs.

## Quick start

Requirements: Python 3.11+

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

### Example API flow

```bash
curl -X POST http://127.0.0.1:8000/documents \
  -F "file=@examples/sample_docs/engineering-handbook.md"

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the deployment review process?","top_k":3}'
```

The local prototype stores documents in memory, so data resets when the process restarts. This is intentional for a compact learning demo.

## Repository map

| Path | Purpose |
|---|---|
| `curriculum/` | Fundamentals-to-production lessons |
| `app/` | Runnable FastAPI reference implementation |
| `tests/` | Unit and API tests |
| `evaluation/` | Small evaluation set and metric guidance |
| `docs/` | Architecture, security, deployment, operations |
| `examples/` | Sample source documents and API requests |
| `projects/` | Portfolio-grade extension briefs |
| `templates/` | Design and evaluation templates |

## Learning path

1. Read `curriculum/00-roadmap.md`.
2. Work through ingestion and chunking before adding embeddings.
3. Understand retrieval and citation correctness before connecting an LLM.
4. Add evaluation before changing prompts or models.
5. Harden access control, file handling, and observability before deployment.

## Architecture

```text
Client
  |
  v
FastAPI + authentication boundary
  |
  +--> Document ingestion --> validation --> extraction --> chunking
  |                                                |
  |                                                v
  |                                      metadata + index
  |
  +--> Question --> query normalization --> retrieval
                                              |
                                              v
                                   ranked source chunks
                                              |
                                              v
                                 grounded answer generation
                                              |
                                              v
                                  answer + source citations
```

For production, replace the in-memory store with durable object storage and PostgreSQL + pgvector (or another vector database), run ingestion asynchronously, and isolate each user's documents by tenant and authorization policy.

## Core engineering principles

- **Grounding:** an answer should be supported by retrieved evidence, not merely sound plausible.
- **Citations:** cite the exact chunks used and make citations traceable to document/page/section metadata.
- **Abstention:** if evidence is insufficient, say so instead of fabricating.
- **Evaluation:** measure retrieval quality and answer faithfulness using curated questions.
- **Security:** uploaded files are untrusted input; enforce limits, validate types, isolate tenants, and never execute document content.
- **Privacy:** define retention, deletion, access, encryption, and provider data-handling policies before using real documents.

## Tests

```bash
pytest
```

The tests cover the included deterministic prototype. They do not validate external LLM providers, embedding models, PDF parsing, production databases, or deployment infrastructure.

## Important limitations

- No hosted LLM or embedding API is called.
- Retrieval uses a simple token-overlap baseline, not semantic vector search.
- Only plain text and Markdown are parsed in the demo.
- In-memory storage is not durable or multi-user.
- Authentication, authorization, malware scanning, and production rate limiting are architectural exercises, not complete production controls.

See `docs/production-readiness-checklist.md` before treating this as a deployable service.
