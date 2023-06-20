import os

class ToDoList:

  def __init__(self):
    self.tasks = []
    self.completed = []
    self.failed = []
  
  def add_task(self, task, category, status='In-Progress'):
    self.tasks.append({
      "Task": task,
      "Category": category,
      "Status": status
    })

  def remove_task(self, num):
    if num <= int(len(self.tasks)):
      del self.tasks[num - 1]
    else:
      print("Error: Task number does not exist.")
  
  def list_tasks(self):
    if len(self.tasks) == 0:
      print("","\n There are currently no tasks.")
    else:
      print("\n Current Task List:")
      for i, task in enumerate(self.tasks, start=1):
        print(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}")
        if i == len(self.tasks):
          print("\n")

  def save_tasks(self, filename):
    with open(filename, "w") as file:
      for i, task in enumerate(self.tasks, start=1):
        file.write(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n")
    print(f"Your To-Do List saved to {os.path.abspath(filename)}")

  def update_to_completed(self, task_num):
    if task_num > len(self.tasks):
      print("There are no tasks in the task list")
    else:
      completed_task = self.tasks[task_num - 1]
      completed_task['Status'] = 'Completed'
      self.completed.append(completed_task)
      del self.tasks[task_num - 1]
      print(f"Task {task_num} has been marked as completed - great job!")

  def list_completed(self):
    print("\n Completed Task List:")
    for i, task in enumerate(self.completed, start=1):
      print(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}")
      if i == len(self.completed):
        print("\n")

  def list_failed(self):
    print("\n Failed Task List:")
    for i, task in enumerate(self.failed, start=1):
      print(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}")
      if i == len(self.completed):
        print("\n")

  def update_to_failed(self, task_num):
    if task_num > len(self.tasks):
      print("There are no tasks in the task list")
    else:
      failed_task = self.tasks[task_num - 1]
      failed_task['Status'] = 'Failed'
      del self.tasks[task_num - 1]
      print(f"Task {task_num} has been marked as failed - Don't worry, the day is not over!")


def Main():
  to_do_list = ToDoList()
  while True:
    print("\nGoals - a super simple task manager\n1. Add task\n2. Delete task\n3. List tasks\n4. Save tasks\n5. Update a task's status\n6. Quit")
    try:
      choice = int(input("Which option do you want: "))
      if choice == 1:
        task = input("What task do you want to add: ")
        category = input("Assign a category for the task: ")
        to_do_list.add_task(task, category)
      elif choice == 2:
        remove = int(input("What task number do you want to remove: "))
        to_do_list.remove_task(remove)
      elif choice == 3:
        list_choice = int(input("Enter 1 for 'To Do List', 2 for 'Completed', or 3 for 'Failed: "))
        if list_choice == 1:
          to_do_list.list_tasks()
        elif list_choice == 2:
          to_do_list.list_completed()
        elif list_choice == 3:
          to_do_list.list_failed()
      elif choice == 4:
        filename = input("What do you want to name the file: ")
        to_do_list.save_tasks(filename)
      elif choice == 5:
        task_to_modify = int(input("Enter the task number you want to update the status for: "))
        new_status = int(input("Enter 1 if you completed the task. Enter 2 if you failed: "))
        if new_status == 1:
          to_do_list.update_to_completed(task_to_modify)
        elif new_status == 2:
          to_do_list.update_to_failed(task_to_modify)
        else:
          print("Please choose 1 (completed) or 2 (failed).")
      elif choice == 6:
        break
      else:
        print("Invalid choice. Please enter a valid task number.")
    except ValueError:
      print("Invalid input. Please enter a valid integer choice.")

if __name__ == '__main__':
  Main()
