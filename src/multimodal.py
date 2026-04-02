from __future__ import annotations

from src.rag import answer_question


def answer_multimodal_question(question: str) -> dict:
    """Version simple du RAG multimodal.

    Elle réutilise le pipeline RAG principal, mais prend en charge des documents
    texte, PDF et images présents dans le dossier data/.
    """
    return answer_question(question=question, k=5)
