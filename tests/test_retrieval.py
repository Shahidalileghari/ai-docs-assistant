from app.chunking import split_into_chunks
from app.retrieval import retrieve


def test_retrieval_ranks_relevant_chunk():
    chunks = split_into_chunks("d1", "guide.md",
        "Deployment requires a reviewed pull request. Database backups run nightly.")
    results = retrieve("How does deployment work?", chunks)
    assert results
    assert "Deployment" in results[0][0].text


def test_no_overlap_returns_no_results():
    chunks = split_into_chunks("d1", "guide.md", "The sky is blue.")
    assert retrieve("database migrations", chunks) == []
