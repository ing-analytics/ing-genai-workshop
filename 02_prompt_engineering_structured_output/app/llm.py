import os

from google import genai
from google.genai.types import GenerateContentConfig


PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = "europe-west4"
MODEL_NAME = "gemini-2.5-flash"


client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)


SYSTEM_MESSAGE = """
You are a helpful travel assistant.
Give clear, concise answers and follow the requested output format.
"""


def ask_llm(
    prompt: str,
    system_instruction: str = SYSTEM_MESSAGE,
    temperature: float = 0.7,
    top_k: int = 40,
    top_p: float = 1.0,
    response_mime_type: str | None = None,
    response_schema: dict | None = None,
) -> str:
    """Send a prompt to the LLM and return the text response."""
    config = GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        response_mime_type=response_mime_type,
        response_schema=response_schema,
    )
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=config,
    )
    return response.text
