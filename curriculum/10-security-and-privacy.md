# 10 — Security and privacy

Threats include malicious files, parser exploits, prompt injection embedded in documents, cross-tenant retrieval leakage, insecure deletion, secrets in logs, and unsafe tool execution.

Controls:
- authenticate every request and authorize every document operation;
- enforce tenant filters inside retrieval queries;
- sandbox parsers and set CPU/memory/time limits;
- scan uploads and restrict supported formats;
- treat document text as untrusted evidence;
- never let retrieved instructions grant tool permissions;
- encrypt data in transit and at rest;
- define retention, export, deletion, and provider data policies;
- redact sensitive content from logs and traces.

Prompt injection defenses are layered controls, not a magic system prompt.
