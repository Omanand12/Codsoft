class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("To-Do List is empty.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
