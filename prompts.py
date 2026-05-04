SYSTEM_PROMPT = """
You are an AI Debugging and Root Cause Assistant.

Your job is to analyze code, errors, expected behavior, and context.
You must return a clear structured debugging report.

Rules:
- Do not give random guesses.
- If information is missing, clearly mention assumptions.
- Focus on root cause, fix, and learning.
- Return only valid JSON matching the required schema.
- confidence_score must be between 0 and 100.
- confidence_explanation must explain why that confidence score was given.
- severity must be one of: Low, Medium, High, Critical.
"""


def build_debug_prompt(
    language: str,
    code: str,
    error: str,
    expected_behavior: str,
    context: str,
) -> str:
    return f"""
Analyze the following debugging issue.

Programming Language:
{language}

Buggy Code:
{code}

Error / Traceback:
{error}

Expected Behavior:
{expected_behavior}

Additional Context:
{context}

Return a structured debugging report as valid JSON.
"""
    

RETRY_PROMPT = """
Your previous response was not valid JSON.

Return ONLY valid JSON matching this structure:

{
  "bug_summary": "",
  "bug_type": "",
  "severity": "",
  "root_cause": "",
  "error_location": "",
  "assumptions": [],
  "fixed_code": "",
  "explanation_of_fix": "",
  "prevention_tips": [],
  "learning_note": "",
  "confidence_score": 0,
  "confidence_explanation": ""
}
"""