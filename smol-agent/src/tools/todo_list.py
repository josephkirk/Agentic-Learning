from smolagents import tool

todos = []
done = []

@tool
def add_todos(new_todos: list[str]) -> str:
    """
    Add new tasks to the todo list.
    Args:
        new_todos: A list of strings, where each string is a distinct task to be added.
    Returns:
        A message confirming the number of tasks added and the current total count.
    """
    global todos
    todos.extend(new_todos)
    delim = '\n  - '
    print(f"Todo list:{delim}{delim.join(todos)}")
    return f"Added {len(new_todos)} to todo list. Now have {len(todos)} todos."

@tool
def mark_todo_done(todo: str) -> str:
    """
    Mark a specific task as completed.
    Args:
        todo: The exact string of the task to mark as done. Must match an item in the current todo list.
    Returns:
        A confirmation message if successful, or an error message if the task was not found.
    """
    global todos, done
    if todo in todos:
        todos.remove(todo)
        done.append(todo)
        return f"Marked the following todo as done:\n  {todo}"
    else:
        return f"Todo list doesn't include todo:\n  {todo}"

@tool
def check_done_todos() -> str:
    """
    Retrieve the list of completed tasks.
    Returns:
        A string representation of the list of completed tasks, or a message indicating no tasks are done.
    """
    if done:
        return str(done)
    else:
        return "No tasks have been marked done."

@tool
def check_todos() -> str:
    """
    Retrieve the current list of pending tasks.
    Returns:
        A string representation of the list of pending tasks, or a message indicating the list is empty.
    """
    if todos:
        return str(todos)
    else:
        return "The todo list is empty."
