from typing import List

from pydantic import BaseModel, Field


class DebugReport(BaseModel):
    bug_summary: str = Field(description="Short summary of the bug")
    bug_type: str = Field(description="Type/category of bug")
    severity: str = Field(description="Low, Medium, High, or Critical")
    root_cause: str = Field(description="Main reason the bug happened")
    error_location: str = Field(description="Likely file, line, function, or code area")
    assumptions: List[str] = Field(
        description="Assumptions made due to missing or unclear information"
    )
    fixed_code: str = Field(description="Corrected code")
    explanation_of_fix: str = Field(description="Why the fix works")
    prevention_tips: List[str] = Field(description="Tips to avoid this bug")
    learning_note: str = Field(description="Short beginner-friendly learning note")
    confidence_score: int = Field(description="Confidence score from 0 to 100")
    confidence_explanation: str = Field(
        description="Reason behind the confidence score"
    )
