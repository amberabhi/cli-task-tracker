from datetime import datetime
import sys, os, json

TASK_FILES = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILES) or os.path.getsize(TASK_FILES) == 0:
        with open(TASK_FILES, "w") as f:
            json.dump([], f)
    
    with open(TASK_FILES, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILES, "w") as f:
        json.dump(tasks, f, indent=2)

def add_tasks(tasks, args):
    if not args:
        print("Please provide a descripiton for the task")
        return
    
    description = args[0]
    timestamp = datetime.now().isoformat()
    new_id = max([task["id"] for task in tasks], default=0) + 1

    new_task = {
        "id" : new_id,
        "status" : "todo",
        "description" : description,
        "created-at" : timestamp,
        "updated-at" : timestamp,
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"New task added successfully with id :{new_id}")

def list_tasks(tasks,args):
    if args:
        status_filter = args[0]
    else:
        status_filter = None

    valid_statuses = ["todo", "in-progress", "done"]
    filtered_tasks = tasks

    if status_filter:
        if status_filter not in valid_statuses:
            print(f"Invalid status. Use one of : {', '.join(valid_statuses)}")
            return
        
        filtered_tasks = []
        for task in tasks:
            if task["status"] == status_filter:
                filtered_tasks.append(task)
        
        if not filtered_tasks:
            print("No tasks found")
            return

        
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']}")
        print(f"  Status    : {task['status']}")
        print(f"  createdAt : {task['created-at']}")
        print()

def update_status(tasks, args, status):
    if not args:
        print(f"please provide task id to mark task as {status}:)")
        return
    
    try:
        task_id = int(args[0])
    except ValueError:
        print("Task id must be a number")
        return
    
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated-at"] = datetime.now().isoformat()
            found = True
            break

    if found :
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status} ✨")
    else :
        print(f"No task found as task id : {task_id}")

def delete_task(tasks, args):
    if not args:
        print("Please provide task id to delete a particular task")
        return
    
    try:
        new_id = int(args[0])
    except ValueError:
        print("Task id must be a no")
        return
    
    new_tasks = []
    for task in tasks:
        if task["id"] != new_id:
            new_tasks.append(task)

    save_tasks(new_tasks)
    print(f"Task with id {new_id} deleted successfully ✨")
        
def update_description(tasks, args):
    if not args:
        print(f"Please provide task id to change its description.")
        return 
    
    try: 
        new_id = int(args[0])
    except ValueError:
        print("Task id should be number")
        return
    
    for task in tasks:
        if task["id"] == new_id:
            print(f"Old description : {task["description"]}")
            updated_description = input("Enter new description : ")
            task["description"] = updated_description
            break

    save_tasks(tasks)
    print(f"description updated successfully✨")

def search_tasks(tasks, args):
    if not args:
        print(f"Please provide keyword u wish to search for:")
        return
    
    keyword = " ".join(args).lower()

    found_tasks = []
    for task in tasks:
        if keyword in task["description"].lower():
            found_tasks.append(task)

    if found_tasks:
        print(f"Found {len(found_tasks)} matching tasks....")
        for task in found_tasks:
            print(f"- [{task['status']}] (ID: {task['id']}) {task['description']}")
    else:
        print("No matching tasks were found.")

def show_help():
    print("""
📋 Task CLI Usage:

Commands:
  add "description"        Add a new task
  list [status]            List all tasks (optionally filter by: todo, done, in-progress)
  mark-done <id>           Mark a task as done
  mark-in-progress <id>    Mark a task as in progress
  update <id>              Update the description of a task
  delete <id>              Delete a task by id
  search "keyword"         Search tasks by keyword in description
  help                     Show this help menu
""")


def main():
    #function to load tasks
    tasks = load_tasks()

    if len(sys.argv) < 2:
        show_help()

    command = sys.argv[1]
    args = sys.argv[2:]

    # calling functions for respective commands 
    if command == "add":
        add_tasks(tasks, args)

    elif command == "list":
        list_tasks(tasks, args)

    elif command == "mark-done":
        status = "done"
        update_status(tasks, args, status)

    elif command == "mark-in-progress":
        status = "in-progress"
        update_status(tasks, args, status)

    elif command == "delete-task":
        delete_task(tasks, args)

    elif command == "update-description":
        update_description(tasks, args)

    elif command == "search":
        search_tasks(tasks, args)
    
    else:
        print("Unknown command !")
        show_help()

if __name__ == "__main__":
    main()