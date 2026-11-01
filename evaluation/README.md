# Evaluation

Build a versioned evaluation set with:
- representative answerable questions;
- unanswerable questions that should trigger abstention;
- expected source document and page/section;
- expected key facts, not one exact wording;
- adversarial questions involving stale or conflicting documents.

Track retrieval Recall@k, Precision@k, MRR, citation precision, answer faithfulness, answer relevance, abstention precision/recall, latency, and cost. Evaluate retrieval separately from generation so failures can be diagnosed.

Never use an LLM judge as the only quality signal. Combine human-reviewed gold labels, deterministic checks, and model-assisted evaluation with periodic audits.
