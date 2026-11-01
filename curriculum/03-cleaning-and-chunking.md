# 03 — Cleaning and chunking

A chunk is a retrieval unit, not just an arbitrary substring. Preserve heading paths, page numbers, table context, and document identity.

## Strategies
- Fixed token windows: predictable but may split concepts.
- Recursive splitting: prefer paragraph, sentence, then token boundaries.
- Structure-aware splitting: use headings, pages, and sections.
- Parent-child retrieval: search small child chunks, then provide a larger parent section to generation.

Overlap can preserve context across boundaries but increases index size and duplicate retrieval. Tune it using evaluation, not intuition alone.

## Exercise
Compare 300, 600, and 1,000-token chunks on the same evaluation set. Record Recall@5, citation quality, latency, and index size.
