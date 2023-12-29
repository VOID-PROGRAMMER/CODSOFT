class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added successfully!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for index, task_info in enumerate(self.tasks, start=1):
                task_status = "✓" if task_info['completed'] else " "
                print(f"{index}. [{task_status}] {task_info['task']}")

    def mark_as_completed(self, task_index):
        try:
            task_info = self.tasks[task_index - 1]
            task_info['completed'] = True
            print(f"Task '{task_info['task']}' marked as completed.")
        except IndexError:
            print("Invalid task index.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            todo_list.show_tasks()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_as_completed(task_index)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
