RESEARCH_KEYWORDS = [
    "paper",
    "papers",
    "research",
    "study",
    "studies",
    "journal",
    "article",
    "author",
    "authors",
    "citation",
    "citations",
    "cite",
    "reference",
    "references",
    "doi",
    "bibtex",
    "apa",
    "mla",
    "ieee",
    "related paper",
    "similar paper",
    "seminal",
    "review paper",
]


RESEARCH_PREFIXES = [
    "doi:",
    "recommend:",
    "network:",
]


def router(state):

    question = state["question"].strip().lower()

    if (
        any(question.startswith(prefix) for prefix in RESEARCH_PREFIXES)
        or any(keyword in question for keyword in RESEARCH_KEYWORDS)
    ):
        state["route"] = "citation"
    else:
        state["route"] = "rag"

    print(f"Selected route: {state['route']}")

    return state