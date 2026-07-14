"""
Citation Tool

Provides high-level research capabilities for the application.

Responsibilities
----------------
- Search academic papers
- Retrieve complete paper information
- Find related papers
- Discover seminal papers
- Explore citation networks

Architecture

Application
        ↓
Citation Tool
        ↓
MCP Client
        ↓
OpenAlex MCP Server
"""

from src.mcp.client import call_tool


def search_papers(
    query: str,
    exact_phrase: bool = False,
):
    """
    Search academic papers.
    """

    result = call_tool(
        tool_name="search_works",
        params={
            "query": query,
            "exact_phrase": exact_phrase,
        },
    )

    return result.content[0].text


def get_paper(work_id: str):
    """
    Retrieve complete information about a paper.

    Accepts:
    - OpenAlex ID
    - DOI
    - OpenAlex URL
    """

    result = call_tool(
        tool_name="get_work",
        params={
            "id": work_id,
        },
    )

    return result.content[0].text


def recommend_papers(
    work_id: str,
    per_page: int = 10,
):
    """
    Retrieve papers related to a given paper.
    """

    result = call_tool(
        tool_name="get_related_works",
        params={
            "id": work_id,
            "per_page": per_page,
        },
    )

    return result.content[0].text


def find_classic_papers(
    topic: str,
    exact_phrase: bool = False,
):
    """
    Find seminal/foundational papers for a topic.
    """

    result = call_tool(
        tool_name="find_seminal_papers",
        params={
            "query": topic,
            "exact_phrase": exact_phrase,
        },
    )

    return result.content[0].text


def get_citation_network(
    work_id: str,
    max_citing: int = 25,
    max_references: int = 25,
):
    """
    Retrieve the citation network of a paper.
    """

    result = call_tool(
        tool_name="get_citation_network",
        params={
            "id": work_id,
            "max_citing": max_citing,
            "max_references": max_references,
        },
    )

    return result.content[0].text