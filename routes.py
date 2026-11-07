from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.app.agents.research_agent import conduct_research

router = APIRouter(
    prefix="/api/v1/research",
    tags=["Autonomous Research Agent"]
)


class ResearchRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=500)
    max_sources: int = Field(default=5, ge=1, le=5)


@router.post("/run")
async def run_research(request: ResearchRequest):
    try:
        return conduct_research(
            request.question,
            request.max_sources
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Autonomous research could not be completed"
        )
