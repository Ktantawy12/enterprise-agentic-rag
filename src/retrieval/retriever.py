from src.vectordb.chroma_db import load_vector_store
def retrieve_documents(query: str, k: int = 5):
    """
    Retrieves the most relevant documents for a query.
    """
    vector_store = load_vector_store()
    results = vector_store.similarity_search(
        query=query,
        k=k,
    )

    return results


if __name__ == "__main__":
    documents = retrieve_documents(
        "What documents are required for a personal loan?"
    )

    print(f"Retrieved {len(documents)} documents.")