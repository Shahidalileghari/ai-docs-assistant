# 04 — Embeddings and vector search

An embedding maps text to a numeric vector. Similarity search retrieves vectors close to the query vector. It is useful for semantic matches, but it can miss exact identifiers, numbers, and rare terms.

## Similarity
Cosine similarity compares vector direction; dot product and Euclidean distance are alternatives. The correct metric depends on model training and vector normalization.

## Production pattern
PostgreSQL + pgvector can keep relational metadata and vectors together. Store embedding model/version and dimensions. Re-embed when changing model versions; do not compare incompatible vector spaces.

## Exercise
Add an `EmbeddingProvider` interface and a fake deterministic provider for tests. Implement a real provider only behind configuration and secrets management.
