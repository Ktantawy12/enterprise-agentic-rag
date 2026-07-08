from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
    """
    Returns the language model.
    """

    return ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )


if __name__ == "__main__":

    llm = get_llm()

    response = llm.invoke("Say hello!")

    print(response.content)