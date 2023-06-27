import os
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:

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
            messagebox.showerror("Error", "Task number does not exist.")

    def list_tasks(self):
        if len(self.tasks) == 0:
            messagebox.showinfo("Task List", "There are currently no tasks.")
        else:
            task_list = "\nCurrent Task List:\n\n"
            for i, task in enumerate(self.tasks, start=1):
                task_list += f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n\n"
            messagebox.showinfo("Task List", task_list)

    def save_tasks(self):
        now = datetime.now()
        month = now.strftime("%B")
        year = str(now.year)
        folder_name = f"Goals - {year}"
        filename = f"{month}{now.strftime('%d')}.txt"
        desktop_path = str(Path.home() / "Desktop")
        folder_path = os.path.join(desktop_path, folder_name, month)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w") as file:
            file.write("Current Task List:\n\n")
            for i, task in enumerate(self.tasks, start=1):
                file.write(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n")
            file.write("\nCompleted Task List:\n\n")
            if len(self.completed) == 0:
                file.write("--none--\n")
            else:
                for i, task in enumerate(self.completed, start=1):
                    file.write(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n")
            file.write("\nFailed Task List:\n\n")
            if len(self.failed) == 0:
                file.write("--none--\n")
            else:
                for i, task in enumerate(self.failed, start=1):
                    file.write(f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n")
        messagebox.showinfo("Task List", f"Your To-Do List saved to {os.path.abspath(file_path)}")

    def update_to_completed(self, task_num):
        if task_num > len(self.tasks):
            messagebox.showerror("Error", "There are no tasks in the task list.")
        else:
            completed_task = self.tasks[task_num - 1]
            completed_task['Status'] = 'Completed'
            self.completed.append(completed_task)
            del self.tasks[task_num - 1]
            messagebox.showinfo("Task Status Update", f"Task {task_num} has been marked as completed - great job!")

    def update_to_failed(self, task_num):
        if task_num > len(self.tasks):
            messagebox.showerror("Error", "There are no tasks in the task list.")
        else:
            failed_task = self.tasks[task_num - 1]
            failed_task['Status'] = 'Failed'
            self.failed.append(failed_task)
            del self.tasks[task_num - 1]
            messagebox.showinfo("Task Status Update", f"Task {task_num} has been marked as failed.")

    def list_completed(self):
        if len(self.completed) == 0:
            messagebox.showinfo("Completed Task List", "--none--")
        else:
            completed_list = "\nCompleted Task List:\n\n"
            for i, task in enumerate(self.completed, start=1):
                completed_list += f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n\n"
            messagebox.showinfo("Completed Task List", completed_list)

    def list_failed(self):
        if len(self.failed) == 0:
            messagebox.showinfo("Failed Task List", "--none--")
        else:
            failed_list = "\nFailed Task List:\n\n"
            for i, task in enumerate(self.failed, start=1):
                failed_list += f"{i}. {task['Task']} | Category: {task['Category']} | Status: {task['Status']}\n\n"
            messagebox.showinfo("Failed Task List", failed_list)

    def create_save_button(self):
        button = tk.Button(text="Save Tasks", command=self.save_tasks)
        button.pack()

def main():
    to_do_list = ToDoListGUI()
    root = tk.Tk()
    root.title("Goals - Task Manager")

    def add_task():
        task = task_entry.get()
        category = category_entry.get()
        to_do_list.add_task(task, category)
        task_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    def remove_task():
        remove = int(remove_entry.get())
        to_do_list.remove_task(remove)
        remove_entry.delete(0, tk.END)

    def list_tasks():
        to_do_list.list_tasks()

    def update_status():
        task_to_modify = int(task_num_entry.get())
        new_status = status_var.get()
        if new_status == 1:
            to_do_list.update_to_completed(task_to_modify)
        elif new_status == 2:
            to_do_list.update_to_failed(task_to_modify)
        else:
            messagebox.showerror("Error", "Please choose 1 (completed) or 2 (failed).")
        task_num_entry.delete(0, tk.END)

    def list_completed():
        to_do_list.list_completed()

    def list_failed():
        to_do_list.list_failed()

    task_label = tk.Label(root, text="Task:")
    task_label.pack()
    task_entry = tk.Entry(root)
    task_entry.pack()

    category_label = tk.Label(root, text="Category:")
    category_label.pack()
    category_entry = tk.Entry(root)
    category_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack()

    list_button = tk.Button(root, text="List Tasks", command=list_tasks)
    list_button.pack()

    task_num_label = tk.Label(root, text="Task Number to Update:")
    task_num_label.pack()
    task_num_entry = tk.Entry(root)
    task_num_entry.pack()

    status_var = tk.IntVar()
    completed_radio = tk.Radiobutton(root, text="Completed", variable=status_var, value=1)
    completed_radio.pack()
    failed_radio = tk.Radiobutton(root, text="Failed", variable=status_var, value=2)
    failed_radio.pack()

    update_button = tk.Button(root, text="Update Status", command=update_status)
    update_button.pack()

    completed_button = tk.Button(root, text="List Completed", command=list_completed)
    completed_button.pack()

    failed_button = tk.Button(root, text="List Failed", command=list_failed)
    failed_button.pack()

    to_do_list.create_save_button()

    root.mainloop()

if __name__ == '__main__':
    main()
