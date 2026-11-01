import pytest
from app.chunking import split_into_chunks


def test_empty_document_has_no_chunks():
    assert split_into_chunks("d1", "empty.txt", "  ") == []


def test_chunks_cover_content_and_have_stable_ids():
    text = "alpha beta gamma " * 100
    chunks = split_into_chunks("d1", "notes.txt", text, chunk_size=100, overlap=20)
    assert len(chunks) > 1
    assert chunks[0].chunk_id == "d1:chunk:0"
    assert all(chunk.text for chunk in chunks)


def test_invalid_overlap_rejected():
    with pytest.raises(ValueError):
        split_into_chunks("d1", "x.txt", "hello", chunk_size=10, overlap=10)
