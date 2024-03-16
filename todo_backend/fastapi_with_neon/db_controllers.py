from sqlmodel import Session, select, Sequence
from .utils import engine
from .db_structure import Todo


def get_todos():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        if not todos:
            return "Todos not found. \n Please Try Again..."
        return todos
    
def add_todo(todo: str):
    with Session(engine) as session:
        db_todo: Todo = Todo(todo_name=todo)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)

        allTodos = session.exec(select(Todo)).all()
        # print("=============================================================")
        # print("All Todos")
        # print(allTodos)
        # print("=============================================================")
        return allTodos


def complete_todo(id: int, todo_status: bool):
    with Session(engine) as session:
        # table = select(Todo).where(Todo.todo_id == id)
        # todo = session.exec(table).one()
        todo = session.get(Todo, id)
        if not todo:
            return f"Could not find todo from ID: {id}"
        todo.todo_status = todo_status
        session.add(todo)
        session.commit()
        session.refresh(todo)

        allTodos = session.exec(select(Todo)).all()
        # print("=============================================================")
        # print("All Todos")
        # print(allTodos)
        # print("=============================================================")

        return allTodos


def delete_todo(id: int):
    with Session(engine) as session:
        # table = select(Todo).where(Todo.todo_id == id)
        # todo = session.exec(table).one()
        todo = session.get(Todo, id)
        if not todo:
            return f"Could not find todo from ID: {id}"
        session.delete(todo)
        session.commit()

        allTodos = session.exec(select(Todo)).all()
        # print("=============================================================")
        # print("All Todos")
        # print(allTodos)
        # print("=============================================================")

        return allTodos
