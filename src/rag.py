from dotenv import load_dotenv
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def load_documents(data_dir="data"):
    docs = []
    data_path = Path(data_dir)

    if not data_path.exists():
        raise ValueError(f"Le dossier {data_dir} est introuvable.")

    files = list(data_path.iterdir())
    if not files:
        raise ValueError(f"Aucun fichier trouvé dans {data_dir}.")

    for file in files:
        if file.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file))
            docs.extend(loader.load())
        elif file.suffix.lower() == ".txt":
            loader = TextLoader(str(file), encoding="utf-8")
            docs.extend(loader.load())

    if not docs:
        raise ValueError("Aucun contenu exploitable trouvé dans les documents.")

    return docs


def build_vectorstore(data_dir="data"):
    docs = load_documents(data_dir)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def answer_question(question: str, data_dir="data") -> str:
    vectorstore = build_vectorstore(data_dir)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    retrieved_docs = retriever.invoke(question)

    if not retrieved_docs:
        return "Aucun passage pertinent n'a été trouvé dans le document."

    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
Tu es un assistant RAG.
Réponds uniquement à partir du contexte suivant.

Contexte :
{context}

Question :
{question}

Réponse :
"""

    response = llm.invoke(prompt)
    return response.content