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
    # ADK's runner is async; this also lets MCP tools share the app's event loop.
    agent = Agent(
        name=APP_NAME,
        model=MODEL_NAME,
        instruction=SYSTEM_MESSAGE,
        tools=tools or [],
    )

    session_service = InMemorySessionService()
    session_id = str(uuid.uuid4())
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=agent,
        session_service=session_service,
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            return "\n".join(
                part.text
                for part in event.content.parts
                if part.text
            )

    return ""
