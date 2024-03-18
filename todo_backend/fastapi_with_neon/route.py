# Import necessary modules
from fastapi import (FastAPI, Body, HTTPException, Depends)
from typing import Annotated
from .db_controllers import (add_todo, delete_todo, complete_todo, get_todos)
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from contextlib import asynccontextmanager
from .db_connector import db_connector, get_session
from .const import origins

# Define an asynchronous context manager for application lifespan
# This logic will be executed once before the application starts receiving requests


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_connector()  # Initialize database connection
    yield

# Initialize FastAPI application with the defined lifespan logic
app = FastAPI(lifespan=lifespan)


# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define main endpoint returning a welcome message


@app.get("/")
def main():
    return {"Home": "Welcome to the FasApi Project!"}

# Endpoint to retrieve all todos


@app.get("/gettodos")
async def getTodo(session: Annotated[Session, Depends(get_session)]):
    todos = get_todos(session)
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)

# Endpoint to create a new todo


@app.post("/createTodo")
async def createTodo(todo: Annotated[str, Body()], session: Annotated[Session, Depends(get_session)]):
    todos: list[dict] = add_todo(todo, session)
    if todos:
        return todos
    return "Todo not found"

# Endpoint to delete a todo


@app.delete("/deleteTodo")
async def deleteTodo(todo_id: int, session: Annotated[Session, Depends(get_session)]):
    todos = delete_todo(todo_id, session)
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)

# Endpoint to mark a todo as completed


@app.put("/completeTodo/{todo_id}")
async def completeTodo(todo_id: int, todo_status: Annotated[bool, Body()], session: Annotated[Session, Depends(get_session)]):
    todos: list[dict] | str = complete_todo(todo_id, todo_status, session)
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)
