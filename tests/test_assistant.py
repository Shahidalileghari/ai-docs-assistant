from app.assistant import answer_question
from app.chunking import split_into_chunks


def test_answer_contains_citations_when_grounded():
    chunks = split_into_chunks("doc-1", "handbook.md",
        "A deployment requires an approved pull request and a successful CI pipeline.")
    result = answer_question("What is required for deployment?", chunks)
    assert result["grounded"] is True
    assert result["citations"][0]["document_id"] == "doc-1"


def test_assistant_abstains_without_evidence():
    result = answer_question("What is the moon made of?", [])
    assert result["grounded"] is False
    assert result["citations"] == []
