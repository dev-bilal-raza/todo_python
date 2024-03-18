# Import necessary modules
from sqlmodel import Session, select
from .db_structure import Todo

# ================================= Function to retrieve all todos from the database ========================================
def get_todos(session: Session):
    # Execute a select query to retrieve all todos
    allTodos = session.exec(select(Todo)).all()
    # If no todos found, return a message
    if not allTodos:
        return "Todos not found. \n Please Try Again..."
    # Otherwise, return all todos
    return allTodos
# ===========================================================================================================================


# ==================================== Function to add a new todo to the database ===========================================
def add_todo(todo: str, session: Session):
    # Create a new Todo object with the given todo string
    db_todo: Todo = Todo(todo_name=todo)
    # Add the new todo to the session
    session.add(db_todo)
    # Commit the transaction to the database
    session.commit()
    # Refresh the todo object to get its updated state from the database
    session.refresh(db_todo)
    # Retrieve all todos from the database
    allTodos = session.exec(select(Todo)).all()
        
    # print("=============================================================")
    # print("All Todos")
    # print(allTodos)
    # print("=============================================================")
   
    # Return all todos
    return allTodos
# ===========================================================================================================================


# ==================================== Function to mark a todo as completed or incomplete ===================================
def complete_todo(id: int, todo_status: bool, session: Session):
    # table = select(Todo).where(Todo.todo_id == id)
    # todo = session.exec(table).one()
    
    # Retrieve the todo object with the given ID
    todo = session.get(Todo, id)
    # If no todo found, return a message
    if not todo:
        return f"Could not find todo from ID: {id}"
    # Update the todo status
    todo.todo_status = todo_status
    # Add the updated todo to the session
    session.add(todo)
    # Commit the transaction to the database
    session.commit()
    # Refresh the todo object to get its updated state from the database
    session.refresh(todo)
    # Retrieve all todos from the database
    allTodos = session.exec(select(Todo)).all()    
   
    # print("=============================================================")
    # print("All Todos")
    # print(allTodos)
    # print("=============================================================")
   
    # Return all todos
    return allTodos
# ===========================================================================================================================


# ====================================== Function to delete a todo from the database ========================================
def delete_todo(id: int, session: Session):
    # Retrieve the todo object with the given ID
    todo = session.get(Todo, id)
    # If no todo found, return a message
    if not todo:
        return f"Could not find todo from ID: {id}"
    # Delete the todo from the session
    session.delete(todo)
    # Commit the transaction to the database
    session.commit()
    # Retrieve all todos from the database
    allTodos = session.exec(select(Todo)).all()
    
    # print("=============================================================")
    # print("All Todos")
    # print(allTodos)
    # print("=============================================================")
    
    # Return all todos
    return allTodos
# ===========================================================================================================================