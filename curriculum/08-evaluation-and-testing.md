# 08 — Evaluation and testing

Test each pipeline stage independently:
- parsing: extraction completeness and page mapping;
- chunking: boundary quality and metadata preservation;
- retrieval: Recall@k, Precision@k, MRR;
- generation: faithfulness, relevance, completeness;
- citations: source correctness and claim support;
- abstention: correct refusal for unanswerable questions;
- operations: latency, errors, token use, and cost.

Use fixed datasets and compare versions. A prompt change, parser update, embedding change, or chunking change can regress quality.
