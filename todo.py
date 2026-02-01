def add_task(tasks, task):
    tasks.append(task)
    print(f"Task added: {task}")

def main():
    print("Welcome to the To-Do List Application")
    tasks = []
    
    add_task(tasks, "Learn Git Commands")
    add_task(tasks, "Create a project")
    
    print("\nYour Tasks:")
    for task in tasks:
        print(f"- {task}")

if __name__ == "__main__":
    main()
