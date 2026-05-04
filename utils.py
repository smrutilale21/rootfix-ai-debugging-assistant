import json
from datetime import datetime
from typing import Any, Dict


def clean_json_response(text: str) -> str:
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1).strip()

    if text.startswith("```"):
        text = text.replace("```", "", 1).strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    return text


def parse_json(text: str) -> Dict[str, Any]:
    cleaned = clean_json_response(text)
    return json.loads(cleaned)


def build_download_report(
    language: str,
    code: str,
    error: str,
    expected_behavior: str,
    context: str,
    result: Dict[str, Any],
) -> str:
    report = {
        "timestamp": datetime.now().isoformat(),
        "input": {
            "language": language,
            "code": code,
            "error": error,
            "expected_behavior": expected_behavior,
            "context": context,
        },
        "debug_report": result,
    }

    return json.dumps(report, indent=2)