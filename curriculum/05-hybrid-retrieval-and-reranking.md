# 05 — Hybrid retrieval and reranking

Combine lexical retrieval (BM25/full text) with semantic vector search. This helps balance exact phrase matching with conceptual similarity.

A typical pipeline:
1. Apply tenant and document ACL filters before retrieval.
2. Fetch candidate chunks from lexical and vector indexes.
3. Fuse rankings (for example reciprocal rank fusion).
4. Rerank a small candidate set with a cross-encoder or model.
5. Deduplicate overlapping chunks and enforce a context budget.

Never retrieve globally and filter authorization only after results are returned to the application.
