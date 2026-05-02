tasks = ()

def menu():
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    print("5. Exit")

def add_task():
    global tasks
    
    new_task = input("Enter a new task: ")
    
    # Add task to tuple
    tasks = tasks + (new_task,)
    
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nTasks:")
        for task in tasks:
            print(task)

def delete_task():
    global tasks
    
    task_to_delete = input("Enter the task to delete: ")
    
    if task_to_delete in tasks:
        # Create new tuple without deleted task
        tasks = tuple(task for task in tasks if task != task_to_delete)
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def update_task():
    global tasks
    
    old_task = input("Enter the task to update: ")
    
    if old_task in tasks:
        new_task = input("Enter the new task: ")
        
        updated_tasks = ()
        
        for task in tasks:
            if task == old_task:
                updated_tasks += (new_task,)
            else:
                updated_tasks += (task,)
        
        tasks = updated_tasks
        print("Task updated successfully.")
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