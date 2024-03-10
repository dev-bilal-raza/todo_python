import { createContext } from "react";
import { Todo } from "@/components/interfaces";
export const todoctx = createContext(
    {
        todo: [{
            todo_id: 0,
            todo_name : "",
            todo_status: false
        }],
        setTodo: (todo: Todo[]) => { }
    }
)