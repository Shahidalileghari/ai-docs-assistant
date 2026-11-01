# Troubleshooting

- `pip install` fails: verify Python 3.11+ and network access to package index.
- `uvicorn` not found: activate the virtual environment and install `.[dev]`.
- Upload returns 415: only `.txt` and `.md` are supported in this demo.
- Upload returns 413: the demo limit is 1 MB.
- No answer: verify the uploaded document contains matching terms; lexical retrieval is intentionally basic.
- Data disappears after restart: expected, because the demo uses in-memory storage.
- Tests fail on import: install the development extra with `pip install -e ".[dev]"`.
