from smolagents import CodeAgent, DuckDuckGoSearchTool, VisitWebpageTool, InferenceClientModel, TransformersModel
from src.tools.todo_list import add_todos, mark_todo_done, check_done_todos, check_todos
from src.tools.file_ops import write_file, create_folder
from src.tools.blender_ops import run_blender_script
from datetime import datetime
import sys
import os
from dotenv import load_dotenv

load_dotenv()

prompt = f"""
You are a helpful assistant working for a busy executive.
Your tone is friendly but direct, they prefer short clear and direct writing.
You try to accomplish the specific task you are given.
You can use any of the tools available to you.
Before you do any work you always make a plan using your Todo list.
You write any temporary files you need to write to complete the task into "Intermediate" folderm, create the folder if not exists.
You write any requested files you need to write to complete the task into "Output" folder, create the folder if not exists.
You always check if the requested result exists before you mark it as done.
You can mark todos off on your todo list after they are complete.


You summarize the actions you took by checking the done list then create a report.
You always ask your assistant to check_done_todos. If they say you are done you send the report to the user.
If your assistant has feedback you add it to your todo list.

Today is {datetime.now()}
"""

def main():
    goal = sys.argv[1] if len(sys.argv) > 1 else "I want to learn about building agents without a framework."
    
    # Use InferenceClientModel as requested.
    model = InferenceClientModel(model_id="Qwen/Qwen3-Coder-480B-A35B-Instruct")

    # model = TransformersModel(
    #     model_id="HuggingFaceTB/SmolLM-135M-Instruct",
    #     temperature=0.7,
    #     max_new_tokens=1000
    # )
    agent = CodeAgent(
        tools=[add_todos, mark_todo_done, check_done_todos, check_todos, DuckDuckGoSearchTool(), VisitWebpageTool(), write_file, create_folder, run_blender_script],
        model=model,
        add_base_tools=True,
        max_steps=20
    )
    
    
    # Inject our custom prompt into the system prompt template.
    # We replace {{custom_instructions}} if it exists, otherwise we prepend it.
    system_prompt_template = agent.prompt_templates["system_prompt"]
    if "{{custom_instructions}}" in system_prompt_template:
        agent.prompt_templates["system_prompt"] = system_prompt_template.replace("{{custom_instructions}}", prompt)
    else:
        agent.prompt_templates["system_prompt"] = prompt + "\n" + system_prompt_template

    print(f"Goal: {goal}")
    print("#" * 40)
    
    result = agent.run(goal)
    
    print("\n\n" + "#" * 40)
    print(f"Answer: {result}")

if __name__ == "__main__":
    main()
