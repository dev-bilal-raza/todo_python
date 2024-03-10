from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated
from .db_controllers import add_todo, delete_todo, complete_todo
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
    return {"message": "Hello World"}


@app.post("/createTodo")
async def createTodo(todo: Annotated[str, Body()]):
    todos: list[dict] = add_todo(todo)
    if todos:
        return todos
    return "Todo not found"


@app.post("/deleteTodo")
async def deleteTodo(todo_id: Annotated[int, Body()]):
    todos: list[dict] = delete_todo(todo_id)
    if todos:
        return todos
    return "Todo not found"


class CompletedTodo(BaseModel):
    todo_id: int
    todo_status: bool


@app.post("/completeTodo")
async def completeTodo(todo_details: CompletedTodo):
    todos: list[dict] = complete_todo(
        todo_details.todo_id, todo_details.todo_status)
    if todos:
        return todos
    return "Todo not found"
