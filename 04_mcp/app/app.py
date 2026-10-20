import argparse
import asyncio
import sys
from pathlib import Path

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from prompt_toolkit import prompt, HTML
from prompt_toolkit.completion import WordCompleter

from agent import ask_agent
from tools import get_weather
from utils import format_response

# Example travel topics for autocompletion
travel_completer = WordCompleter([
    "I love art and museums",
    "Looking for good food spots",
    "Find cheap flights to Tokyo",
    "Estimate daily budget in Amsterdam",
], ignore_case=True)

SERVER_SCRIPT = Path(__file__).parent / "server.py"

mcp_tools = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command=sys.executable,
            args=[str(SERVER_SCRIPT.resolve())],
        ),
        timeout=10.0,
    )
)

local_tools = [get_weather]


async def run_assistant(user_prompt: str) -> str:
    try:
        available_tools = await mcp_tools.get_tools()
        print("Available MCP tools:")
        for tool in available_tools:
            print(f"- {tool.name}: {tool.description}")

        return await ask_agent(
            user_prompt,
            tools=[mcp_tools, *local_tools],
        )
    finally:
        await mcp_tools.close()


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
