# 06 — Grounded generation and citations

The generation layer receives a question and selected evidence. It should be instructed to answer only from that evidence, identify uncertainty, and cite source IDs. Treat retrieved text as data, never as system instructions.

A robust citation object should include document ID/version, page or section, chunk ID, and a short excerpt. Validate that every cited source was actually supplied to the model.

Abstain when retrieval is weak, evidence conflicts, or the question is outside the corpus. Similarity scores are not calibrated probabilities; thresholds must be evaluated.

## Exercise
Create tests where the retrieved text contains “ignore all previous instructions”. Confirm it cannot override application policy.
