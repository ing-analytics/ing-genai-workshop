import argparse
from pathlib import Path

from dotenv import load_dotenv
from prompt_toolkit import prompt, HTML
from prompt_toolkit.completion import WordCompleter

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


def run_assistant(user_prompt: str) -> str:
    from llm import ask_llm
    return ask_llm(user_prompt)


def main() -> None:
    parser = argparse.ArgumentParser(description="Travel Assistant")
    parser.add_argument("prompt", type=str, nargs="?", help="User travel query prompt")
    args = parser.parse_args()

    if not args.prompt:
        user_prompt = prompt(HTML('<skyblue>Enter your travel query:</skyblue> '), completer=travel_completer)
    else:
        user_prompt = args.prompt

    print("\n=== Travel Assistant ===\n")
    response = run_assistant(user_prompt)
    format_response(response)
    print("\n")

if __name__ == "__main__":
    main()
