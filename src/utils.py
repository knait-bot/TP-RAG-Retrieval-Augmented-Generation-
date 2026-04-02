from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

import fitz
from langchain_core.documents import Document
from pypdf import PdfReader

from src.config import (
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_PDF_EXTENSIONS,
    SUPPORTED_TEXT_EXTENSIONS,
)


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def read_pdf_file(path: Path) -> str:
    try:
        reader = PdfReader(str(path))
        parts: list[str] = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        text = "\n".join(parts).strip()
        if text:
            return text
    except Exception:
        pass

    doc = fitz.open(str(path))
    parts = [page.get_text("text") for page in doc]
    return "\n".join(parts).strip()


def describe_image_file(path: Path) -> str:
    return (
        f"Image trouvée : {path.name}. "
        "Cette image a été ajoutée dans la base documentaire du projet multimodal. "
        "Le système peut la référencer comme ressource visuelle associée au dossier."
    )


def load_documents_from_directory(data_dir: Path) -> List[Document]:
    docs: list[Document] = []
    for path in sorted(data_dir.glob("*")):
        if path.suffix.lower() in SUPPORTED_TEXT_EXTENSIONS:
            text = read_text_file(path)
        elif path.suffix.lower() in SUPPORTED_PDF_EXTENSIONS:
            text = read_pdf_file(path)
        elif path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS:
            text = describe_image_file(path)
        else:
            continue

        if text.strip():
            docs.append(
                Document(
                    page_content=text,
                    metadata={"source": path.name, "path": str(path)},
                )
            )
    return docs


def format_sources(documents: Iterable[Document]) -> str:
    seen = []
    for doc in documents:
        src = doc.metadata.get("source", "document inconnu")
        if src not in seen:
            seen.append(src)
    return ", ".join(seen) if seen else "Aucune source"
