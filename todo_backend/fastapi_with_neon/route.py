from fastapi import (FastAPI, Body, HTTPException)
from typing import Annotated
from .db_controllers import (add_todo, delete_todo, complete_todo, get_todos)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    todos = get_todos()
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)


@app.post("/createTodo")
async def createTodo(todo: Annotated[str, Body()]):
    todos: list[dict] = add_todo(todo)
    if todos:
        return todos
    return "Todo not found"


@app.delete("/deleteTodo")
async def deleteTodo(todo_id: int):
    todos= delete_todo(todo_id)
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)


@app.put("/completeTodo/{todo_id}")
async def completeTodo(todo_id: int, todo_status: Annotated[bool, Body()]):
    todos: list[dict] | str = complete_todo(
        todo_id, todo_status)
    if not type(todos) == str:
        return todos
    raise HTTPException(status_code=404, detail=todos)
