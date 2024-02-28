import csv
import sys
import requests

def export_tasks_to_csv(user_id):
    # Fetch data from API
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks = response.json()

    # Write data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([task["userId"], users[task["userId"]]["username"], task["completed"], task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_tasks_to_csv(user_id)
