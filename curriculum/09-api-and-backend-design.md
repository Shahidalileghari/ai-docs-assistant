# 09 — API and backend design

Separate document, ingestion-job, chunk, collection, conversation, and message resources. Long-running extraction and embedding should use background workers rather than blocking upload requests.

Useful endpoints:
- `POST /documents` — create upload.
- `GET /documents` — list authorized documents.
- `DELETE /documents/{id}` — delete source and derived indexes.
- `GET /jobs/{id}` — ingestion status.
- `POST /conversations/{id}/ask` — ask within authorized scope.

Use idempotency keys for retryable jobs, pagination for lists, request IDs for tracing, and explicit lifecycle states.
