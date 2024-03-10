import React from 'react'
import { Todo } from '@/components/interfaces'
import useTodo from './context/TodoProvider'



const TodoItem = () => {
    const { todo, setTodo } = useTodo()

    const deletedTodo = async (todo_id: number) => {
        // console.log(todo_id);
        const response = await fetch("http://localhost:8000/deleteTodo", {
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify(todo_id)
        })
        const data: Todo[] = await response.json();
        // console.log(data);
        setTodo(data)
    }
    const toggleTodo = async (todo_id: number, todo_status: boolean) => {
        // console.log(todo_id, todo_status);
        const response = await fetch("http://localhost:8000/completeTodo", {
            method: "POST",
            headers: {
                "content-type": "application/json",
            },

            body: JSON.stringify({
                "todo_id": todo_id,
                "todo_status": todo_status
            })
        })
        const data: Todo[] = await response.json();
        // console.log(data);
        setTodo(data)

    }

    return (
        <div className='  bg-[radial-gradient(ellipse_at_bottom,_var(--tw-gradient-stops))] from-gray-500 via-slate-300 to-slate-900 text-black w-2/6 rounded-lg   p-5'>

            {todo.map((todo) => (
                <div key={todo.todo_id} className='mb-3 flex gap-x-3 px-4 py-2 border-black/10 rounded-lg bg-[#48505ce2] '>
                    <input type="checkbox"
                        checked={todo.todo_status}
                        onChange={() => toggleTodo(todo.todo_id, !todo.todo_status)}
                    />
                    <h1
                        className={`border font-light text-lg  w-full text-white rounded-md border-white/30 px-2  ${todo.todo_status ? "line-through decoration-2 decoration-[#222C3B]" : ""}`}
                    >
                        {todo.todo_name.charAt(0).toUpperCase() + todo.todo_name.slice(1)}
                    </h1>

                    <button className="inline-flex w-8 h-8 rounded-lg text-sm border border-black/10 justify-center items-center bg-gray-50 hover:bg-gray-100 shrink-0"
                        onClick={() => deletedTodo(todo.todo_id)}
                    >❌</button>
                </div>
            ))}
        </div>
    )
}

export default TodoItem