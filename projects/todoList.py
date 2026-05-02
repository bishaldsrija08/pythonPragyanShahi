tasks = []

def menu():
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    print("5. Exit")
    
def add_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)

def view_tasks():
    if not tasks: # Check if the tasks list is empty
        print("No tasks to show.")
    else:
        for task in tasks:
            print(task)

def delete_task():
    task_to_delete = input("Enter the task to delete: ")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
    else:
        print("Task not found.")

def update_task():
    old_task = input("Enter the task to update:")
    if old_task in tasks:
        new_task = input("Enter the new task:")
        index = tasks.index(old_task) # Find the index of the old task
        tasks[index] = new_task # Update the task at the found index with the new task
    else:
        print("Task not found.")
        
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        update_task()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")