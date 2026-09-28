from pathlib import Path


class DocumentIngestionService:
    def __init__(self, documents_path: str = "data/documents"):
        self.documents_path = Path(documents_path)

    def load_documents(self) -> list[dict]:
        documents = []

        for file_path in self.documents_path.glob("*.md"):
            content = file_path.read_text(encoding="utf-8")

            documents.append(
                {
                    "filename": file_path.name,
                    "content": content,
                }
            )

        return documents
