from smolagents import tool
import os

@tool
def write_file(content: str, filename: str) -> str:
    """
    Writes content to a file with the given filename.
    Args:
        content: The text content to write to the file.
        filename: The name of the file to save (e.g., 'script.py', 'notes.md').
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"

@tool
def create_folder(folder_path: str) -> str:
    """
    Creates a new folder at the specified path.
    Args:
        folder_path: The path of the folder to create.
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Successfully created folder: {folder_path}"
    except Exception as e:
        return f"Error creating folder: {str(e)}"
