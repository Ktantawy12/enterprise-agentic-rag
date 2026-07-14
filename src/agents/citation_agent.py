"""
Citation Agent

Handles research-related requests using OpenAlex.

Architecture

User
    ↓
Citation Agent
    ↓
Citation Tool
    ↓
MCP Client
    ↓
OpenAlex
"""

from src.graph.state import ResearchState
from src.agents.citation_formatter import format_results

from src.tools.citation_tool import (
    search_papers,
    get_paper,
    recommend_papers,
    find_classic_papers,
    get_citation_network,
)


def citation_agent(state: ResearchState):

    question = state["question"].strip()
    question_lower = question.lower()

    if question_lower.startswith("recommend:"):
        

        work_id = question.split(":", 1)[1].strip()
        answer = recommend_papers(work_id)

    elif question_lower.startswith("network:"):
        

        work_id = question.split(":", 1)[1].strip()
        answer = get_citation_network(work_id)

    elif question_lower.startswith("doi:"):

        work_id = question.split(":", 1)[1].strip()
        answer = get_paper(work_id)

    elif question_lower.startswith("https://openalex.org/"):

        answer = get_paper(question)



    elif (
        "seminal" in question_lower
        or "foundational" in question_lower
        or "classic" in question_lower
    ):

        answer = find_classic_papers(question)

    elif (
        "paper" in question_lower
        or "papers" in question_lower
        or "research" in question_lower
        or "article" in question_lower
    ):

        answer = search_papers(question)

    else:

        return {
            "answer": (
                "I couldn't determine the requested research action.\n\n"
                "Examples:\n"
                "- Find papers about LangGraph\n"
                "- Find seminal papers about RAG\n"
                "- DOI:10.xxxx/xxxxx\n"
                "- recommend:https://openalex.org/W123456789\n"
                "- network:https://openalex.org/W123456789"
            )
        }

    formatted_answer = format_results(answer)

    return {
        "answer": formatted_answer,
    }