# 01 — Problem and architecture

A document assistant is not simply a chat UI attached to a PDF. It is a pipeline that converts unstructured files into searchable evidence and uses that evidence to answer a scoped question.

## RAG flow
1. Ingest and validate a file.
2. Extract text and structure.
3. Split content into retrievable chunks.
4. Enrich chunks with metadata and embeddings.
5. Retrieve relevant chunks for a question.
6. Optionally rerank results.
7. Generate an answer constrained by evidence.
8. Return citations and confidence/abstention metadata.

## Why RAG?
Fine-tuning changes model behavior; it is not the normal way to keep a private document collection current. RAG retrieves relevant external knowledge at query time. It supports source updates and citations, but quality depends on parsing, chunking, retrieval, and generation.

## Exercise
Draw a sequence diagram for upload and ask flows. Mark trust boundaries, durable stores, and points where user authorization is enforced.
