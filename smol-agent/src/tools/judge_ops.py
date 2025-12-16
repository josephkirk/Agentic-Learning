from smolagents import tool
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

@tool
def check_goal_done(goal: str, answer: str) -> str:
    """
    Evaluates if the provided answer successfully fulfills the stated goal using an LLM judge.
    Args:
        goal: The original objective or task description.
        answer: The final result or answer provided by the agent.
    Returns:
        A JSON string containing:
        - 'done': boolean indicating if the goal is met.
        - 'feedback': A list of strings with specific feedback or reasons for failure.
    """
    # Use a capable model for judging. 
    # Valid model IDs from HF: 'Qwen/Qwen2.5-Coder-32B-Instruct' is good.
    model_id = "Qwen/Qwen2.5-Coder-32B-Instruct" 
    
    # Check for token
    token = os.getenv("HF_TOKEN")
    if not token:
        return "Error: HF_TOKEN environment variable not found. Please set your Hugging Face token in the .env file to use the judge."
        return "Error: HF_TOKEN environment variable not set."

    client = InferenceClient(model=model_id, token=token)

    system_prompt = """
You are a research assistant who reads requests and answers.
You determine if the answer satisfies the request.
If it does you respond that the request is done.
If not you give specific feedback on what is missing in the form of actionable individual todos.

You must output a valid JSON object with the following structure:
{
    "done": boolean,
    "feedback": ["actionable todo 1", "actionable todo 2"]
}
"""
    
    user_prompt = f"## Request: {goal}\n\n## Answer: {answer}"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = client.chat_completion(
            messages=messages, 
            max_tokens=500,
            temperature=0.1
        )
        content = response.choices[0].message.content
        
        # Cleanup code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[0].strip() # This might be risky if it splits beginning. Better logic useful.
            # actually if it starts with ```json it enters first if. 
            # if it's just ``` it enters here.
            # simpler:
            pass
            
        clean_content = content.strip()
        if clean_content.startswith("```json"):
            clean_content = clean_content[7:]
        if clean_content.startswith("```"):
            clean_content = clean_content[3:]
        if clean_content.endswith("```"):
            clean_content = clean_content[:-3]
        
        clean_content = clean_content.strip()

        # basic validation
        json.loads(clean_content)
        
        return clean_content
    except Exception as e:
        return f"Error running LLM judge: {str(e)}"
