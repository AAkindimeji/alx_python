import json
import sys
import requests

def export_tasks_to_json(user_id):
    # Fetch data from API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks = response.json()

    # Organize tasks by user ID
    tasks_by_user = {}
    for task in tasks:
        if task["userId"] not in tasks_by_user:
            tasks_by_user[task["userId"]] = []
        tasks_by_user[task["userId"]].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": users[task["userId"]]["username"]
        })

    # Write data to JSON file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump(tasks_by_user, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_tasks_to_json(user_id)
