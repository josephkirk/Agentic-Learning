from smolagents import tool
import subprocess
import os

@tool
def run_blender_script(script_path: str, save_path: str = "output.blend") -> str:
    """
    Executes a Python script enabling Blender to perform 3D operations.
    Run in background mode, so no UI is visible.
    Args:
        script_path: The absolute or relative path to the Python script to execute.
        save_path: The absolute or relative path where the resulting Blender file (.blend) should be saved. Defaults to 'output.blend'.
    Returns:
        A formatted string containing the standard output (stdout) and standard error (stderr) from the Blender process.
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
