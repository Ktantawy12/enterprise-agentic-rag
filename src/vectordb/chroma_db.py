import os

from langchain_chroma import Chroma

from src.chunking.splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model


DB_PATH = "chroma_db"


def create_vector_store():
    """
    Creates a new Chroma vector database from the document chunks.
    """

    chunks = split_documents()

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_PATH,
    )

    return vector_store


def load_vector_store():
    """
    Loads an existing Chroma vector database.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model,
    )

    return vector_store


def load_or_create_vector_store():
    """
    Loads the vector database if it exists,
    otherwise creates it.
    """

    if os.path.exists(DB_PATH):
        print("Loading existing vector database...")
        return load_vector_store()

    print("Creating new vector database...")
    return create_vector_store()


if __name__ == "__main__":

    vector_store = load_or_create_vector_store()

    data = vector_store.get()

    print(f"\nTotal indexed documents: {len(data['documents'])}")