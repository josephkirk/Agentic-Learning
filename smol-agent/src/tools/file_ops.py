from smolagents import tool
import os

@tool
def write_file(content: str, filename: str) -> str:
    """
    Writes text content to a file. 
    IMPORTANT: This will overwrite the file if it already exists.
    Args:
        content: The text content to write.
        filename: The absolute or relative path to the file (e.g., 'Output/script.py').
    Returns:
        A success message or an error message.
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
    Creates a new directory at the specified path. 
    Safe to call if the folder already exists.
    Args:
        folder_path: The absolute or relative path of the folder to create.
    Returns:
        A success message or an error message.
    """
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Successfully created folder: {folder_path}"
    except Exception as e:
        return f"Error creating folder: {str(e)}"
