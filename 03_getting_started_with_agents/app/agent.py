import os
import uuid

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types


LOCATION = "europe-west4"
MODEL_NAME = "gemini-2.5-flash"

os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "true")
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", LOCATION)

APP_NAME = "Travel_Assistant"
USER_ID = "workshop-user"


# Set a default system message for the model
SYSTEM_MESSAGE = """
    You are a helpful travel assistant.
    You have access to tools. Decide whether you need to use a tool.
    - If needed, use it
    - Otherwise, answer directly
"""


async def ask_agent(
    prompt: str,
    tools: list | None = None,
) -> str:
    """Run one ADK agent turn and return its final response text."""
    # TODO EXERCISE: Build an ADK Agent using the model, system instruction, and tools.
    # TODO EXERCISE: Create an in-memory session, then create a Runner for the agent.
    # TODO EXERCISE: Wrap prompt as a user Content message and run the agent.
    # TODO EXERCISE: Return text from the final response event.
    raise NotImplementedError("Complete the ADK agent exercise.")
