"use client"
import { FormEvent, useRef } from 'react'
import TodoItem from './TodoItem'
import React from 'react'
import { Todo } from '@/components/interfaces'
import useTodo from './context/TodoProvider'

const TodoForm = () => {
  const { setTodo } = useTodo()
  const ref = useRef<HTMLInputElement>(null);
  
  const formSubmit = async (f: FormEvent) => {
    f.preventDefault();
    const input_value: string = ref.current!.value;
    const response = await fetch("http://localhost:8000/createTodo", {
      method: "POST",
      headers: {
        "request-mode": "no cors",
        "content-type": "application/json"
      },
      body: JSON.stringify(input_value)
    })
    const todos: Todo[] = await response.json()
    if (todos) {
      setTodo(todos)
    }

  }
  return (
    <div className='flex flex-col items-center gap-10'>
      <h1 className="text-6xl font-semibold bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 inline-block text-transparent bg-clip-text">
        TODO FORM
      </h1>
      <form onSubmit={formSubmit}>
        <div className='flex'>
          <input
            className='w-[20vw] border-black/10 outline-none duration-150 bg-white/20 rounded-l-lg px-3 py-1.5 '
            type="text"
            placeholder='Write Todo'
            ref={ref}
          />
          <button className='rounded-r-lg px-3 py-1 bg-green-600 hover:bg-green-500 text-white shrink-0' type='submit'> Add</button>
        </div>
      </form>
      <TodoItem />
    </div>
  )
}

export default TodoForm