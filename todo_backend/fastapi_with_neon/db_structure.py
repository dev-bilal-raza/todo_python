# Import necessary modules
from sqlmodel import SQLModel, Field

# ================================= In this file I am creating a table structure for our database ==============================
class Todo(SQLModel, table=True):
    todo_id: int | None = Field(None, primary_key=True)
    todo_name: str
    todo_status: bool = False
# ==============================================================================================================================    
    