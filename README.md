# ing-genai-workshop

Practical exercises for the GenAI Workshop run by ING Analytics


## Setup

### GitHub Codespaces

1. On GitHub, select **Code > Codespaces > Create codespace on main** (or your workshop branch), and wait for setup to finish.
2. The dev container installs Python 3.12, the Google Cloud CLI, the Python/Pylance/Jupyter extensions, and the workshop dependencies in `.venv`. New terminals use this environment automatically.
3. Configure your workshop project and Google credentials in the terminal:

```bash
bash scripts/setup_gcloud.sh <PROJECT_ID>
```

Follow the authentication links in the terminal in your browser. If a browser cannot open automatically, rerun the affected `gcloud auth` command with `--no-launch-browser` and follow its prompts.

For notebooks, select **Python (ING GenAI Workshop)** from the kernel picker. Credentials are not included in the container; each student signs in separately.

The same configuration works locally with VS Code's **Dev Containers: Reopen in Container** command and Docker installed.

### Local Setup

Use Python 3.11 or newer.

1. Configure Google authentication and project access from One Day Sandbox

```bash
bash scripts/setup_gcloud.sh <PROJECT_ID>
```

2. Create and activate the Python environment:

```bash
bash scripts/setup_venv.sh
source .venv/bin/activate
```

3. Make sure the virtual environment is active before running any app or notebook.

## Exercises

- `01_getting_started_with_llm/` — basic direct LLM usage with `google.genai`.
  - Teaches prompt construction, system instructions, and a simple `ask_llm()` wrapper.

- `03_getting_started_with_agents/` — ADK agent with tool usage.
  - Shows how to build an agent and pass tools.

- `04_mcp/` — ADK + MCP server integration.
  - Demonstrates exposing reusable tools through an MCP server and discovering/using tools from an agent.

## Notes

- `scripts/install_gcloud.sh` installs only the Google Cloud CLI without interactive prompts, project configuration, or authentication. The dev container runs it automatically; locally, run `bash scripts/install_gcloud.sh` and open a new Bash terminal to use `gcloud`.
- `scripts/setup_gcloud.sh` configures `gcloud`, logs in with the workshop WIF login config, and enables the AI Platform API.
The workshop uses Application Default Credentials/Vertex AI rather than API keys.
- `scripts/setup_venv.sh` creates a `.venv` virtual environment and installs requirements from `requirements.txt`.