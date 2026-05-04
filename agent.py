import os

from dotenv import load_dotenv
from openai import OpenAI

from logger import setup_logger
from prompts import RETRY_PROMPT, SYSTEM_PROMPT, build_debug_prompt
from schemas import DebugReport
from utils import parse_json

load_dotenv()

logger = setup_logger()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def analyze_bug(
    language: str,
    code: str,
    error: str,
    expected_behavior: str,
    context: str,
) -> DebugReport:
    user_prompt = build_debug_prompt(
        language=language,
        code=code,
        error=error,
        expected_behavior=expected_behavior,
        context=context,
    )

    try:
        logger.info("Sending debug analysis request to LLM")

        response = client.chat.completions.create(
            model=MODEL,
            temperature=0.2,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
        )

        raw_output = response.choices[0].message.content
        parsed_output = parse_json(raw_output)

        return DebugReport(**parsed_output)

    except Exception as first_error:
        logger.warning(f"First attempt failed: {first_error}")

        try:
            logger.info("Retrying with stricter JSON prompt")

            retry_response = client.chat.completions.create(
                model=MODEL,
                temperature=0,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                    {"role": "user", "content": RETRY_PROMPT},
                ],
                response_format={"type": "json_object"},
            )

            raw_retry_output = retry_response.choices[0].message.content
            parsed_retry_output = parse_json(raw_retry_output)

            return DebugReport(**parsed_retry_output)

        except Exception as retry_error:
            logger.error(f"Retry failed: {retry_error}")
            raise RuntimeError(
                "Debug analysis failed. Please check your input and try again."
            ) from retry_error
