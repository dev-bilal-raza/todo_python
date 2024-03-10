"use client"
import { todoctx } from "./todoCtx";
import { useState, useContext } from "react";
import { Todo } from "@/components/interfaces";

export const TodoProvider = ({ children }: {
	children: React.ReactNode
}) => {
	const [todo, setTodo] = useState<Todo[]>([]);

	return (
		<todoctx.Provider value={{ todo, setTodo }}>
			{children}
		</todoctx.Provider>
	)
}
export default function useTodo() {
	return useContext(todoctx)
}