import re
from collections import Counter


STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "is", "are",
    "was", "were", "be", "been", "being", "to", "of", "in",
    "on", "for", "with", "as", "by", "at", "from", "that",
    "this", "these", "those", "it", "its", "they", "them",
    "their", "we", "our", "you", "your", "he", "she", "his",
    "her", "which", "who", "what", "when", "where", "how",
    "why", "can", "could", "will", "would", "should", "may",
    "might", "has", "have", "had", "do", "does", "did",
    "not", "no", "so", "than", "then", "also", "such",
    "into", "about", "over", "under", "after", "before",
    "between", "through", "there", "here", "all", "any"
}


def analyze_content(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("Content cannot be empty")

    words = re.findall(r"\b[a-zA-Z0-9'-]+\b", text.lower())

    if not words:
        raise ValueError("No readable words found")

    if len(words) > 20000:
        raise ValueError("Content exceeds the 20,000-word analysis limit")

    word_count = len(words)

    # Extract important keywords
    meaningful_words = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    frequencies = Counter(meaningful_words)

    keywords = [
        {"keyword": word, "frequency": count}
        for word, count in frequencies.most_common(10)
    ]

    # Sentence extraction
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = [
        sentence.strip()
        for sentence in sentences
        if len(sentence.split()) >= 5
    ]

    # Simple extractive summary
    summary = sentences[:3]

    reading_time = max(1, round(word_count / 200))

    return {
        "summary": summary,
        "keywords": keywords,
        "word_count": word_count,
        "sentence_count": len(sentences),
        "estimated_reading_time_minutes": reading_time,
        "analysis_status": "completed"
    }
