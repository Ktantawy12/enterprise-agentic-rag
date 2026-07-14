"""
Tool Selector

Uses the LLM to decide which OpenAlex tool
should handle the user's request.
"""

from langchain_core.prompts import ChatPromptTemplate

from src.llm.llm import llm


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert routing assistant.

Choose exactly ONE tool.

Available tools:

search_papers
- Search academic papers.

get_paper
- Retrieve detailed information about one paper.

recommend_papers
- Recommend papers related to an existing paper.

find_classic_papers
- Find seminal/foundational papers.

get_citation_network
- Show papers citing or cited by another paper.

Return ONLY the tool name.

No explanation.
            """,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)


selector = prompt | llm


def select_tool(question: str) -> str:

    response = selector.invoke(
        {
            "question": question,
        }
    )

    return response.content.strip()