# To do list - App 
import os

# Create a todolist class
class ToDoList:

  def __init__(self):
    self.tasks = []
  
  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, num):
    if num <= int(len(self.tasks)):
      del self.tasks[num - 1]
    else:
      print("Error: Task number does not exist.")
  
  def list_tasks(self):
    for i, task in enumerate(self.tasks, start=1):
      print(f"{i}. {task}")

  def save_tasks(self, filename):
    with open(filename, "w") as file:
      for i, task in enumerate(self.tasks, start=1):
        file.write(f"{i}. {task} \n")
    print(f"Your To-Do List saved to {os.path.abspath(filename)}")

# Write Main function
def Main():
  to_do_list = ToDoList()
  while True:
    print("\n1. Add task\n2. Delete task\n3. List tasks\n4. Save tasks\n5. Exit")
    choice = int(input("Which option do you want: "))
    if choice == 1:
      task = input("What task do you want to add: ")
      to_do_list.add_task(task)
    elif choice == 2:
      remove = int(input("What task number do you want to remove: "))
      to_do_list.remove_task(remove)
    elif choice == 3:
      to_do_list.list_tasks()
    elif choice == 4:
      filename = input("What do you want to name the file: ")
      to_do_list.save_tasks(filename)
    elif choice == 5:
      break
    else:
      print("Invalid choice. Please enter a valid task number.")

if __name__ == '__main__':
  Main()
