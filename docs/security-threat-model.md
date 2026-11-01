# Security threat model

| Asset | Threat | Primary control |
|---|---|---|
| Private documents | Cross-tenant access | ACL filtering in every query |
| Upload service | Malformed or malicious file | Type/size limits, scanning, sandbox |
| LLM context | Prompt injection in source text | Treat retrieved text as untrusted data |
| API credentials | Secret leakage | Secret manager, redaction, rotation |
| User questions | Abuse/cost exhaustion | Auth, quotas, rate limits, budgets |
| Deleted documents | Residual chunks/vectors | Cascading deletion and verification |

Assume documents may contain hostile instructions. The model must not be able to change authorization policy or invoke privileged tools based on retrieved content.
