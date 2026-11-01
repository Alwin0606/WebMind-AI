from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak
)


def build_markdown_report(research: dict) -> str:
    question = research.get("question", "Research report")
    sources = research.get("sources", [])
    metrics = research.get("metrics", {})

    lines = [
        "# WebMind AI — Research Intelligence Report",
        "",
        f"**Research question:** {question}",
        f"**Generated:** {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Executive Summary",
        "",
    ]

    for index, source in enumerate(sources, start=1):
        lines.extend([
            f"### {index}. {source.get('title') or 'Untitled source'}",
            "",
            source.get("summary", "No summary available."),
            "",
            f"- Source: {source.get('url', '')}",
            f"- Relevance: {source.get('relevance', {}).get('assessment', 'not assessed')}",
            "",
        ])

    lines.extend([
        "## Research Metrics",
        "",
        f"- Sources reviewed: {metrics.get('sources_reviewed', len(sources))}",
        f"- Sources with evidence: {metrics.get('sources_with_evidence', 0)}",
        "",
        "## Key Terms",
        "",
    ])

    for keyword in research.get("key_terms", []):
        lines.append(f"- {keyword}")

    lines.extend([
        "",
        "## Limitations",
        "",
        "This report summarizes retrieved web pages and automated relevance analysis. "
        "Relevance scores are not proof that a claim is true. Important findings should "
        "be checked against original sources.",
        "",
    ])

    return "\n".join(lines)


def build_pdf_report(research: dict, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=0.65 * inch,
        leftMargin=0.65 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title="WebMind AI Research Report",
        author="WebMind AI",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#173B68"),
        spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#176B87"),
        spaceBefore=14,
        spaceAfter=8,
    ))

    story = [
        Paragraph("WEBMIND AI", styles["ReportTitle"]),
        Paragraph("Research Intelligence Report", styles["Heading2"]),
        Spacer(1, 12),
        Paragraph(
            f"<b>Research question:</b> {escape(str(research.get('question', '')))}",
            styles["BodyText"],
        ),
        Paragraph(
            f"<b>Generated:</b> {datetime.now(timezone.utc).isoformat()}",
            styles["BodyText"],
        ),
        Spacer(1, 16),
        Paragraph("Research Findings", styles["SectionHeading"]),
    ]

    for index, source in enumerate(research.get("sources", []), start=1):
        title = escape(str(source.get("title") or "Untitled source"))
        summary = escape(str(source.get("summary") or "No summary available."))
        url = escape(str(source.get("url") or ""))
        relevance = source.get("relevance", {}).get("assessment", "not assessed")

        story.extend([
            Paragraph(f"{index}. {title}", styles["Heading3"]),
            Paragraph(summary, styles["BodyText"]),
            Spacer(1, 5),
            Paragraph(f"<b>Source:</b> {url}", styles["BodyText"]),
            Paragraph(f"<b>Relevance:</b> {escape(str(relevance))}", styles["BodyText"]),
            Spacer(1, 12),
        ])

    metrics = research.get("metrics", {})
    story.extend([
        Paragraph("Research Metrics", styles["SectionHeading"]),
        Paragraph(
            f"Sources reviewed: {metrics.get('sources_reviewed', 0)}",
            styles["BodyText"],
        ),
        Paragraph(
            f"Sources with evidence: {metrics.get('sources_with_evidence', 0)}",
            styles["BodyText"],
        ),
        Paragraph("Key Terms", styles["SectionHeading"]),
        Paragraph(
            escape(", ".join(research.get("key_terms", [])) or "No key terms found."),
            styles["BodyText"],
        ),
        Spacer(1, 14),
        Paragraph("Limitations", styles["SectionHeading"]),
        Paragraph(
            "Automated relevance analysis does not establish factual truth. "
            "Review original sources before relying on important findings.",
            styles["BodyText"],
        ),
    ])

    document.build(story)
    return output_path
