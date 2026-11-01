from fastapi.testclient import TestClient
from app.main import app, store

client = TestClient(app)


def setup_function():
    store.documents.clear()


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_upload_list_ask_and_delete_flow():
    response = client.post("/documents", files={
        "file": ("handbook.md",
                 b"Deployment requires an approved pull request and passing CI.",
                 "text/markdown")
    })
    assert response.status_code == 200
    document_id = response.json()["document_id"]
    assert client.get("/documents").json()[0]["document_id"] == document_id

    answer = client.post("/ask", json={"question": "What does deployment require?"})
    assert answer.status_code == 200
    assert answer.json()["grounded"] is True
    assert answer.json()["citations"]

    deleted = client.delete(f"/documents/{document_id}")
    assert deleted.status_code == 200


def test_rejects_unsupported_extension():
    response = client.post("/documents", files={
        "file": ("payload.exe", b"not executable", "application/octet-stream")
    })
    assert response.status_code == 415
