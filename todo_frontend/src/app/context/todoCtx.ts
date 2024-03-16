import { createContext } from "react";
import { Todo } from "@/components/interfaces";
export const todoctx = createContext(
    {
        todo: [] as Todo[],
        setTodo: (todo: Todo[]) => { }
    }
)