import Image from "next/image";
import TodoForm from "./TodoForm";
export default function Home() {
  return (
    <main className="bg-gradient-to-bl from-slate-900 via-gray-800 to-slate-600 w-full h-screen p-5">
      <TodoForm/>
    </main>
  );
}
