# Architecture decisions

## Prototype
FastAPI routes call a small application service. The in-memory store contains document records and chunks. Retrieval uses token overlap. The answer layer returns passages and source references.

## Production target
- API: FastAPI or another typed web framework.
- Identity: OIDC/OAuth2 with tenant-aware authorization.
- Object storage: S3-compatible private bucket.
- Metadata: PostgreSQL.
- Search: PostgreSQL full-text + pgvector, or dedicated search/vector services.
- Queue: Celery/RQ/Arq or managed queue.
- Workers: isolated extraction and embedding processes.
- Generation: provider adapter with timeouts, retries, budgets, and fallback policy.
- Observability: OpenTelemetry traces, structured logs, metrics.

## Key decision
Keep provider interfaces separate from domain logic. This makes model changes testable and avoids binding business rules to one vendor SDK.
