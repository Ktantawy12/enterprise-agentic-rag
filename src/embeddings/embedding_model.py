from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_embedding_model():
    """
    Returns the OpenAI embedding model.
    """

    return OpenAIEmbeddings(
        model="text-embedding-3-small"
    )


if __name__ == "__main__":
    print("Embedding model initialized successfully!")
    