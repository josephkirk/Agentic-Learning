# smol-agent

A lightweight, agentic AI assistant built using the `smolagents` library. This agent is designed to be a helpful assistant for a busy executive, capable of planning tasks, managing files, and even controlling Blender to 3D tasks.

## Features

- **Task Planning**: The agent uses a built-in Todo list management system to plan, track, and verify its tasks before execution.
- **File Operations**: Capable of writing files and creating directories to organize its work.
- **Blender Integration**: precise control over Blender via Python scripts to automate 3D scene manipulation and asset creation.
- **Web Browsing**: Equipped with DuckDuckGo search and webpage visiting capabilities to gather information.
- **Model Flexibility**: configured to use robust inference models (e.g., Qwen via Hugging Face Inference API).

## Installation

This project uses `uv` for dependency management.

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    uv sync
    ```

## Usage

Run the agent by executing the `main.py` script with your goal as an argument.

```bash
uv run main.py "Your goal here"
```

### Examples

**General Research & File Writing:**
```bash
uv run main.py "Research the history of the 3D printing and write a brief summary to Output/summary.md"
```

**Blender Automation:**
```bash
uv run main.py "run blender script that clean scene , create a sphere and save it as sphere.blend"
# This will save the resulting .blend file to the Output folder (if specified in the plan)
```

## Tools

The agent has access to the following tools:

- `add_todos`: Add items to the todo list.
- `mark_todo_done`: Mark items as complete.
- `check_done_todos`: Review completed tasks.
- `check_todos`: View the current todo list.
- `write_file`: Write text content to a file.
- `create_folder`: Create new directories.
- `run_blender_script`: Execute a Python script within Blender.
- `DuckDuckGoSearchTool`: Search the web.
- `VisitWebpageTool`: Read the content of a webpage.

## Configuration

- **Environment Variables**: Create a `.env` file to store necessary API keys (e.g., Hugging Face tokens).
- **Model**: The model configuration can be adjusted in `main.py`. Currently setup to use `Qwen/Qwen2.5-Coder-32B-Instruct` or similar high-performance models.
