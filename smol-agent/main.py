from smolagents import CodeAgent, DuckDuckGoSearchTool, VisitWebpageTool, InferenceClientModel
from src.tools.todo_list import add_todos, mark_todo_done, check_done_todos, check_todos
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
You can mark todos off on your todo list after they are complete.

You summarize the actions you took by checking the done list then create a report.
You always ask your assistant to check_done_todos. If they say you are done you send the report to the user.
If your assistant has feedback you add it to your todo list.

Today is {datetime.now()}
"""

def main():
    goal = sys.argv[1] if len(sys.argv) > 1 else "I want to learn about building agents without a framework."
    
    # Use InferenceClientModel as requested.
    model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

    agent = CodeAgent(
        tools=[add_todos, mark_todo_done, check_done_todos, check_todos, DuckDuckGoSearchTool(), VisitWebpageTool()],
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
