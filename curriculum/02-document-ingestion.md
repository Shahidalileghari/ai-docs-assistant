# 02 — Document ingestion

Treat a file as hostile input. Validate extension and content, enforce size and page limits, decode safely, scan where appropriate, and store it outside executable paths.

## Pipeline
Upload -> quarantine -> validation -> malware scan -> extraction -> normalization -> metadata -> chunking -> indexing.

Keep original file metadata: tenant, owner, checksum, MIME type, upload time, parser version, document version, and retention policy.

## Parsers
- TXT/Markdown: straightforward decoding and heading-aware parsing.
- PDF: PyMuPDF or pypdf; preserve page numbers and layout hints.
- DOCX: python-docx; preserve headings and tables.
- Scanned PDF: OCR; retain page coordinates and OCR confidence.
- HTML: sanitize and extract meaningful content; do not execute scripts.

## Exercise
Add PDF and DOCX adapters. Reject encrypted, oversized, malformed, or unsupported files with explicit error states.
