"use client"
import TodoForm from "./TodoForm";
import { useEffect, useState } from "react";
import useTodo from "./context/TodoProvider";
import { Todo } from "@/components/interfaces";

export default function Home() {
  const { setTodo } = useTodo()
  useEffect(() => {
    const subscribe = async () => {
      const res = await fetch("http://localhost:8000/gettodos");
      if (res.status === 200) {
        const todos: Todo[] = await res.json();
        setTodo(todos)
      }
    }
    subscribe();

  }, [])

  return (
    <main className="bg-gradient-to-bl from-slate-900 via-gray-800 to-slate-600 w-full h-screen p-5">
        <TodoForm />
    </main>
  );
}
