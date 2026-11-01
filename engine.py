from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> list:
    if not query or not query.strip():
        raise ValueError("Search query cannot be empty")

    max_results = max(1, min(max_results, 10))

    results = DDGS().text(
        query.strip(),
        max_results=max_results
    )

    return [
        {
            "title": item.get("title", ""),
            "url": item.get("href", ""),
            "snippet": item.get("body", "")
        }
        for item in results
    ]
