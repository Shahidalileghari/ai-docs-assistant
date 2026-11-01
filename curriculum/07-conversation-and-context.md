# 07 — Conversation and context

Conversation history helps resolve references such as “compare that with the previous section,” but it can also leak context between users or overwhelm the model context window.

Store conversation ownership and document permissions explicitly. Summarize old turns carefully, preserve source IDs, and re-run retrieval for each substantive follow-up. Do not assume a prior citation remains authorized forever.

## Exercise
Implement a follow-up question resolver while ensuring each turn rechecks current document access.
