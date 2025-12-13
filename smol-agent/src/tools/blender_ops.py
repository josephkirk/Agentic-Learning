from smolagents import tool
import subprocess
import os

@tool
def run_blender_script(script_path: str, save_path: str = "output.blend") -> str:
    """
    Runs a Python script inside Blender in background mode.
    Args:
        script_path: The path to the Python script to execute in Blender.
        save_path: The path where the Blender file should be saved (optional, defaults to output.blend).
    """
    try:
        # Check if python script exists
        if not os.path.exists(script_path):
            return f"Error: Script file '{script_path}' not found."

        # Construct Blender command
        # blender -b -P script.py -- save_path
        # We pass save_path as an argument to the script if needed, 
        # but usually the script handles saving. 
        # Let's assume the script needs to know where to save, so we append the save path as an argument.
        command = ["blender", "-b", "-P", script_path, "--", save_path]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return f"Blender script executed successfully.\nOutput:\n{result.stdout}"
        else:
            return f"Blender execution failed.\nError:\n{result.stderr}\nOutput:\n{result.stdout}"

    except FileNotFoundError:
        return "Error: 'blender' command not found in PATH. Please ensure Blender is installed and added to your system PATH."
    except Exception as e:
        return f"Error running Blender: {str(e)}"
