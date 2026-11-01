
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.app.verification.engine import assess_relevance

router = APIRouter(
    prefix="/api/v1/verification",
    tags=["Claim Verification"]
)


class VerificationRequest(BaseModel):
    claim: str = Field(..., min_length=5, max_length=2000)
    content: str = Field(..., min_length=10, max_length=20000)


@router.post("/verify")
async def verify_claim(request: VerificationRequest):
    try:
        result = assess_relevance(
            request.claim,
            request.content
        )

        return {
            "status": "completed",
            "claim": request.claim,
            "assessment": result,
            "disclaimer": (
                "This is a relevance assessment, not definitive "
                "fact-checking or proof of truth."
            )
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Verification failed: {str(error)}"
        )
