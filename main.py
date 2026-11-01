from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone

from backend.app.search.routes import router as search_router
from backend.app.crawler.routes import router as crawler_router
from backend.app.intelligence.routes import router as intelligence_router
from backend.app.verification.routes import router as verification_router
from backend.app.agents.routes import router as research_router
from backend.app.reports.routes import router as reports_router

app = FastAPI(
    title="WebMind AI",
    description="Beyond Search. Into Intelligence. An AI-powered Internet Research Platform.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)
app.include_router(crawler_router)
app.include_router(intelligence_router)
app.include_router(verification_router)
app.include_router(research_router)
app.include_router(reports_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to WebMind AI",
        "tagline": "Beyond Search. Into Intelligence.",
        "status": "running",
    }


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "WebMind AI Backend",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/v1/system/info")
async def system_info():
    return {
        "platform": "WebMind AI",
        "version": "1.0.0",
        "capabilities": [
            "AI-powered web search",
            "Intelligent web crawling",
            "HTML content extraction",
            "Content summarization",
            "Keyword extraction",
            "Multi-source verification",
            "Autonomous research agent",
            "PDF and Markdown report generation",
        ],
    }
