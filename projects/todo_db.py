# To Do list app with database - CRUD operations

import json

FILE_NAME = 'todo_list.json'

# Function to read todo items

def read_todo():
    try:
        with open(FILE_NAME, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            if isinstance(data, dict):
                return data.get("tasks", [])
            return []
    except FileNotFoundError:
        return []

# Function to save a new todo item

def save_todo(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)
        
# Function to add a new todo item
def add_task(task):
    tasks = read_todo() # Read existing tasks
    new_task = {
        "id": len(tasks)+1,
        "task": task,
        "status": 'pending'
    }
    tasks.append(new_task) # Add new task to the list
    save_todo(tasks) 
    print(f'Task "{task}" added successfully!')

# Function to update an existing todo item
def update_task(task_id, new_task):
    tasks = read_todo()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = new_task
            save_todo(tasks)
            print(f'Task ID {task_id} updated successfully!')
        else:
            print(f'Task ID {task_id} not found.')
# Function to delete a todo item
def delete_task(task_id):
    tasks = read_todo()
    tasks = [task for task in tasks if task["id"] != task_id] # Remove the task with the given ID
    save_todo(tasks)
    print(f'Task ID {task_id} deleted successfully!')

# Main loop to interact with the user
while True:
    print("\nTo Do List App")
    print("1. Add Task")
    print("2. Read Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        tasks = read_todo()
        if tasks:
            print("\nCurrent Tasks:")
            for task in tasks:
                print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")
        else:
            print("No tasks found.")
    elif choice == '3':
        task_id = int(input("Enter the task ID to update: "))
        new_task = input("Enter the new task: ")
        update_task(task_id, new_task)
    elif choice == '4':
        task_id = int(input("Enter the task ID to delete: "))
        delete_task(task_id)
    elif choice == '5':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
