from smolagents import CodeAgent, DuckDuckGoSearchTool, VisitWebpageTool, InferenceClientModel, TransformersModel
from src.tools.todo_list import add_todos, mark_todo_done, check_done_todos, check_todos
from src.tools.file_ops import write_file, create_folder
from src.tools.blender_ops import run_blender_script
from src.tools.judge_ops import check_goal_done
from datetime import datetime
import sys
import os
from dotenv import load_dotenv

load_dotenv()

prompt = f"""
You are a helpful assistant working for a busy executive.
Your tone is friendly but direct; they prefer short, clear, and direct writing.

Your workflow:
1.  **Plan**: Before doing any work, analyze the request and add tasks to your Todo list.
2.  **Execute**: Use your tools to complete the tasks. 
    - Write any requested files to the "Output" folder (create it if missing).
    - Use the Blender tool for 3D tasks.
3.  **Verify**: You MUST use the `check_goal_done` tool to verify your work against the user's goal.
    - If `check_goal_done` returns feedback, add new tasks to your Todo list to fix the issues.
    - Only providing the final answer when `check_goal_done` confirms the goal is met.

Today is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

def main():
    goal = sys.argv[1] if len(sys.argv) > 1 else "I want to learn about building agents without a framework."
    
    # Use a strong, reliable model.
    model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

    agent = CodeAgent(
        tools=[add_todos, mark_todo_done, check_done_todos, check_todos, DuckDuckGoSearchTool(), VisitWebpageTool(), write_file, create_folder, run_blender_script, check_goal_done],
        model=model,
        add_base_tools=True,
        max_steps=20,
        verbosity_level=2
    )
    
    # Prepend our custom instructions to the system prompt.
    agent.prompt_templates["system_prompt"] = prompt + "\n" + agent.prompt_templates["system_prompt"]

    print(f"Goal: {goal}")
    print("#" * 40)
    
    result = agent.run(goal)
    
    print("\n\n" + "#" * 40)
    print(f"Answer: {result}")

if __name__ == "__main__":
    main()
