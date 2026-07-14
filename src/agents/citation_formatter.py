"""
Citation Formatter

Converts raw OpenAlex output into a clean,
concise response for the user.
"""

from langchain_core.prompts import ChatPromptTemplate

from src.llm.llm import get_llm

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an academic research assistant.

You will receive raw search results from OpenAlex.

Your job is to present the information in a professional, concise format.

Rules:

- Never invent information.
- Show only the 5 most relevant papers.
- Ignore metadata and JSON formatting.
- For each paper include:

    • Title
    • Authors
    • Publication Year
    • Citation Count
    • 2-3 sentence summary of why the paper is relevant.

- If a DOI or PDF link exists, include it.

- Format using Markdown headings and bullet points.

- At the end write a short recommendation like:

"Recommended starting paper: ..."

Do not mention OpenAlex.
Do not output JSON.
Keep the answer readable.
"""
        ),
        (
            "human",
            "{result}"
        ),
    ]
)
llm = get_llm()
formatter = prompt | llm


def format_results(result: str) -> str:

    response = formatter.invoke(
        {
            "result": result
        }
    )

    return response.content