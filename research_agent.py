from urllib.parse import urlparse

from backend.app.search.engine import search_web
from backend.app.crawler.engine import extract_page
from backend.app.intelligence.analyzer import analyze_content
from backend.app.verification.engine import assess_relevance


def conduct_research(question: str, max_sources: int = 5) -> dict:
    """
    Coordinate web search, crawling, content analysis,
    and source relevance assessment.
    """

    # Stage 1: Search
    search_results = search_web(question, max_sources * 2)

    sources = []
    visited_domains = set()
    errors = []

    # Stage 2: Crawl and analyze independent sources
    for result in search_results:
        url = result.get("url", "")
        domain = urlparse(url).hostname

        if not domain or domain in visited_domains:
            continue

        visited_domains.add(domain)

        try:
            page = extract_page(url)
            content = page.get("content", "")

            if not content.strip():
                errors.append({
                    "url": url,
                    "error": "No readable content extracted"
                })
                continue

            analysis = analyze_content(content)
            relevance = assess_relevance(question, content)

            sources.append({
                "title": page.get("title", result.get("title", "")),
                "url": url,
                "domain": domain,
                "summary": analysis["summary"],
                "keywords": analysis["keywords"],
                "word_count": analysis["word_count"],
                "relevance_score": relevance["score"],
                "relevance_assessment": relevance["assessment"],
                "evidence": relevance["evidence"]
            })

        except Exception as exc:
            errors.append({
                "url": url,
                "error": str(exc)
            })

        if len(sources) >= max_sources:
            break

    # Stage 3: Consolidate findings
    all_keywords = {}

    for source in sources:
        for item in source["keywords"]:
            keyword = item["keyword"]
            all_keywords[keyword] = (
                all_keywords.get(keyword, 0) + item["frequency"]
            )

    top_keywords = sorted(
        all_keywords.items(),
        key=lambda item: item[1],
        reverse=True
    )[:10]

    relevant_sources = [
        source for source in sources
        if source["relevance_assessment"] in (
            "high_relevance",
            "partial_relevance"
        )
    ]

    report_sections = []

    for index, source in enumerate(sources, start=1):
        report_sections.append({
            "section": index,
            "title": source["title"],
            "summary": source["summary"],
            "source_url": source["url"],
            "relevance": source["relevance_assessment"]
        })

    return {
        "research_question": question,
        "research_status": (
            "completed" if sources else "no_sources_retrieved"
        ),
        "research_metrics": {
            "sources_retrieved": len(sources),
            "relevant_sources": len(relevant_sources),
            "failed_sources": len(errors)
        },
        "key_topics": [
            {"keyword": word, "frequency": count}
            for word, count in top_keywords
        ],
        "research_report": report_sections,
        "sources": sources,
        "retrieval_errors": errors,
        "limitations": [
            "This report summarizes retrieved web pages.",
            "Relevance scores measure keyword overlap, not truth.",
            "The agent does not independently establish factual accuracy.",
            "Search results and website content may be incomplete or outdated."
        ]
    }
