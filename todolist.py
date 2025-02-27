class Todo_list:
    def __init__(self):
        self.tasks = []

    def addtask(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def viewtasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    def markcompleted(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def deletetask(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.\n")

def main():
    todo_list = Todo_list()
    while True:
        print("To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            todo_list.viewtasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.addtask(task)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.markcompleted(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.deletetask(task_number)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()