export interface Todo {
    todo_id: number,
    todo_name: string,
    todo_status: boolean
}
export interface ErrorType {
    status_code: number,
    detail: string
}