#!/usr/bin/python3
"""
Extend Python script to export data in JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employees = requests.get(url + "/users").json()
    tasks_dict = {}

    for employee in employees:
        user_id = employee.get("id")
        username = employee.get("username")
        tasks = requests.get(url + f"/todos?userId={user_id}").json()

        tasks_list = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            tasks_list.append(task_dict)

        tasks_dict[str(user_id)] = tasks_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)
