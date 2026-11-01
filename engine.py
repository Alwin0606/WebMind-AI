
import re
from collections import Counter


STOP_WORDS = {
    "the", "is", "are", "was", "were", "a", "an", "and",
    "or", "but", "to", "of", "in", "on", "for", "with",
    "by", "at", "from", "as", "it", "this", "that",
    "be", "has", "have", "had", "will", "would", "can",
    "could", "should", "may", "might", "about", "into"
}


def extract_keywords(text: str) -> list[str]:
    """Extract meaningful words from text."""
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())

    return [
        word for word in words
        if word not in STOP_WORDS
    ]


def assess_relevance(claim: str, content: str) -> dict:
    """
    Estimate how relevant source content is to a claim.

    This is a keyword-overlap assessment.
    It does not establish whether a claim is true or false.
    """

    if not isinstance(claim, str) or not claim.strip():
        raise ValueError("Claim cannot be empty.")

    if not isinstance(content, str) or not content.strip():
        raise ValueError("Source content cannot be empty.")

    claim_keywords = set(extract_keywords(claim))
    content_keywords = set(extract_keywords(content))

    if not claim_keywords:
        return {
            "score": 0,
            "label": "Insufficient information",
            "matched_keywords": [],
            "missing_keywords": [],
            "total_claim_keywords": 0,
            "explanation": "No meaningful keywords found in the claim."
        }

    matched = sorted(claim_keywords.intersection(content_keywords))
    missing = sorted(claim_keywords.difference(content_keywords))

    score = round(
        (len(matched) / len(claim_keywords)) * 100,
        2
    )

    if score >= 75:
        label = "High relevance"
    elif score >= 40:
        label = "Moderate relevance"
    else:
        label = "Low relevance"

    return {
        "score": score,
        "label": label,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "total_claim_keywords": len(claim_keywords),
        "matched_keyword_count": len(matched),
        "explanation": (
            "The score measures keyword overlap between the claim "
            "and source content. It is not a truth score."
        )
    }
