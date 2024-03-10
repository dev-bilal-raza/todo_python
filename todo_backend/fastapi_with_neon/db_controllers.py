from sqlmodel import Session, select
from .utils import engine
from .db_structure import Todo


def add_todo(todo: str):
    with Session(engine) as session:
        db_todo: Todo = Todo(todo_name=todo)
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        table = select(Todo)
        allTodos = session.exec(table).all()
        print("All Todos")
        print(allTodos)

        return [{"todo_id": todo.todo_id, "todo_name": todo.todo_name,
            "todo_status": todo.todo_status} for todo in allTodos]


def complete_todo(id: int, todo_status: bool):
    with Session(engine) as session:
        table = select(Todo).where(Todo.todo_id == id)
        todo = session.exec(table).one()
        todo.todo_status = todo_status
        session.add(todo)
        session.commit()
        table = select(Todo)
        allTodos = session.exec(table).all()

        return [{"todo_id": todo.todo_id, "todo_name": todo.todo_name,
            "todo_status": todo.todo_status} for todo in allTodos]



def delete_todo(id: int):
    with Session(engine) as session:
        table = select(Todo).where(Todo.todo_id == id)
        todo = session.exec(table).one()
        session.delete(todo)
        session.commit()
        table = select(Todo)
        allTodos = session.exec(table).all()

        return [{"todo_id": todo.todo_id, "todo_name": todo.todo_name,
            "todo_status": todo.todo_status} for todo in allTodos]

