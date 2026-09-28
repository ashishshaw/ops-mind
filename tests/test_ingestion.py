from app.services.rag.ingestion import DocumentIngestionService


def test_load_documents():
    service = DocumentIngestionService()

    documents = service.load_documents()

    assert len(documents) > 0
    assert documents[0]["filename"].endswith(".md")
    assert documents[0]["content"]
