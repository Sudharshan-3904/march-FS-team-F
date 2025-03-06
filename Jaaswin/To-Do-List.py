
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                print(f'- {task}')

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Read a book")
    todo_list.view_tasks()
    todo_list.remove_task("Buy groceries")
    todo_list.view_tasks()

