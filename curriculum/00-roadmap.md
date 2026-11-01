# Roadmap and prerequisites

## Outcome
Build a grounded document assistant and understand the engineering decisions behind a reliable retrieval-augmented generation (RAG) system.

## Prerequisites
Python, HTTP/REST, JSON, basic databases, Git, and basic ML/LLM concepts. Learn the Python/API foundations first if needed.

## Modules
1. `01-problem-and-architecture.md` — product scope, RAG architecture, trade-offs.
2. `02-document-ingestion.md` — upload pipeline, parsing, metadata, untrusted files.
3. `03-cleaning-and-chunking.md` — normalization, chunk size, overlap, structure.
4. `04-embeddings-and-vector-search.md` — embedding spaces, similarity, pgvector.
5. `05-hybrid-retrieval-and-reranking.md` — lexical + semantic retrieval, filters, rerankers.
6. `06-grounded-generation-and-citations.md` — prompt boundaries, citations, abstention.
7. `07-conversation-and-context.md` — history, follow-up questions, token budgets.
8. `08-evaluation-and-testing.md` — gold sets, retrieval metrics, faithfulness.
9. `09-api-and-backend-design.md` — endpoints, async work, persistence.
10. `10-security-and-privacy.md` — tenant isolation, prompt injection, data governance.
11. `11-production-and-observability.md` — deployment, tracing, cost, latency.
12. `12-advanced-features.md` — OCR, tables, multimodal, agents, workflows.

## Suggested schedule
- Phase 1: lessons 1–3 and run the local prototype.
- Phase 2: lessons 4–6 and implement semantic retrieval + provider adapter.
- Phase 3: lessons 7–9 and add durable storage + background ingestion.
- Phase 4: lessons 10–12 and build evaluation, observability, and deployment.

## Definition of done
A user can upload authorized documents, ask a question, receive an evidence-backed answer with traceable citations, and get a clear abstention when evidence is missing. Tests cover ingestion, access boundaries, retrieval, citations, deletion, and failure modes.
