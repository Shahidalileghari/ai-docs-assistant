# Deployment blueprint

1. Build a non-root container and pin dependencies.
2. Configure PostgreSQL and private object storage.
3. Run schema migrations as a separate release step.
4. Start API and ingestion workers as separate processes.
5. Put TLS termination and request-size limits at the gateway.
6. Configure secrets through the platform secret manager.
7. Add health/readiness checks and queue monitoring.
8. Back up metadata and documents; test restoration.
9. Roll out with staged traffic and a rollback plan.

The included prototype has no production Dockerfile by design; deployment depends on selecting real persistence, identity, and model providers.
