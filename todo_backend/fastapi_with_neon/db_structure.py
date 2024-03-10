from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    todo_id: int | None = Field(None, primary_key=True)
    todo_name: str
    todo_status: bool = False