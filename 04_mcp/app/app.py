import argparse
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from prompt_toolkit import prompt, HTML
from prompt_toolkit.completion import WordCompleter

from agent import ask_agent
from tools import get_weather
from utils import format_response

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")

# Example travel topics for autocompletion
travel_completer = WordCompleter([
    "I love art and museums",
    "Looking for good food spots",
    "Find cheap flights to Tokyo",
    "Estimate daily budget in Amsterdam",
], ignore_case=True)

SERVER_SCRIPT = Path(__file__).parent / "server.py"

# TODO EXERCISE: Configure McpToolset to launch SERVER_SCRIPT using sys.executable and StdioConnectionParams.
mcp_tools = None

local_tools = [get_weather]


async def run_assistant(user_prompt: str) -> str:
    # TODO EXERCISE: Discover and print MCP tools, then pass them with local_tools to ask_agent.
    # TODO EXERCISE: Always close the MCP toolset, including when the agent call fails.
    raise NotImplementedError("Complete the MCP app integration exercise.")


def main():
    parser = argparse.ArgumentParser(description="Travel Assistant")
    parser.add_argument("prompt", type=str, nargs="?", help="User travel query prompt")
    args = parser.parse_args()

    if not args.prompt:
        user_prompt = prompt(HTML('<skyblue>Enter your travel query:</skyblue> '), completer=travel_completer)
    else:
        user_prompt = args.prompt

    print("\n=== Travel Assistant ===\n")
    response = asyncio.run(run_assistant(user_prompt))
    format_response(response)
    print("\n\n")

if __name__ == "__main__":
    main()
