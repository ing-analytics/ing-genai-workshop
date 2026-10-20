import argparse
import asyncio
from prompt_toolkit import prompt, HTML
from prompt_toolkit.completion import WordCompleter

from agent import ask_agent
from tools import get_weather, search_flights
from utils import format_response

# Example travel topics for autocompletion
travel_completer = WordCompleter([
    "I love art and museums",
    "Looking for good food spots",
    "Find cheap flights to Tokyo",
    "Estimate daily budget in Amsterdam",
], ignore_case=True)


async def run_assistant(user_prompt: str) -> str:
    return await ask_agent(
        user_prompt,
        tools=[get_weather, search_flights],
    )


def main():
    parser = argparse.ArgumentParser(description="Travel Assistant")
    parser.add_argument("prompt", type=str, nargs="?", help="User travel query prompt")
    args = parser.parse_args()

    if not args.prompt:
        user_prompt = prompt(HTML('<skyblue>Enter your travel query:</skyblue> '), completer=travel_completer)
    else:
        user_prompt = args.prompt

    print("\n=== Travel Assistant ===\n")    
    # The ADK runner needs to wait for the model and tools to reply.
    # asyncio.run() starts the async work from this regular, synchronous main() function.
    # eg: send prompt -> wait for model/tool replies -> get response -> show it.
    response = asyncio.run(run_assistant(user_prompt))
    format_response(response)
    print("\n\n")

if __name__ == "__main__":
    main()
