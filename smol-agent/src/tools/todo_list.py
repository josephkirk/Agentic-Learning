from smolagents import tool

todos = []
done = []

@tool
def add_todos(new_todos: list[str]) -> str:
    """
    Add an array of todos to the todo list.
    Args:
        new_todos: The array of new todos to add to the todo list.
    """
    global todos
    todos.extend(new_todos)
    delim = '\n  - '
    print(f"Todo list:{delim}{delim.join(todos)}")
    return f"Added {len(new_todos)} to todo list. Now have {len(todos)} todos."

@tool
def mark_todo_done(todo: str) -> str:
    """
    Mark an individual item on the todo list as done.
    Args:
        todo: The todo item to mark as done.
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
    Read everything on the todo list that has been marked done.
    """
    if done:
        return str(done)
    else:
        return "No tasks have been marked done."

@tool
def check_todos() -> str:
    """
    Read everything on the todo list.
    """
    if todos:
        return str(todos)
    else:
        return "The todo list is empty."
