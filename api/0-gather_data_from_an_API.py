import requests

def get_employee_progress(employee_id):
  """
  Gets the TODO list progress for a given employee ID.

  Args:
      employee_id: The ID of the employee.

  Returns:
      A string containing the employee's name, progress information, and completed 
      task titles.
  """

  # Get employee details
  employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  response = requests.get(employee_url)
  employee_data = response.json()

  # Get TODO list
  todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  response = requests.get(todo_url)
  todo_data = response.json()

  # Calculate progress
  completed_tasks = sum(task["completed"] for task in todo_data)
  total_tasks = len(todo_data)
  progress_text = f"done with tasks({completed_tasks}/{total_tasks}):"

  # Format output
  output = f"Employee {employee_data['name']} is {progress_text}\n"
  for task in todo_data:
    if task["completed"]:
      output += f"\t{task['title']}\n"

  return output

if __name__ == "__main__":
  # Get employee ID from command line argument
  if len(sys.argv) != 2:
    print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

  employee_id = int(sys.argv[1])

  # Get and display progress information
  progress = get_employee_progress(employee_id)
  print(progress)
