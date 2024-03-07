import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_task_count()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.delete(task_index)
        update_task_count()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def complete_task():
    try:
        task_index = task_list.curselection()[0]
        task_list.itemconfig(task_index, bg="light green")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def update_task_count():
    task_count_label.config(text=f"Total Tasks: {task_list.size()}")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry widget
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)
remove_button = tk.Button(root, text="Remove Task", width=10, command=remove_task)
remove_button.grid(row=1, column=1, padx=5, pady=5)
complete_button = tk.Button(root, text="Complete Task", width=10, command=complete_task)
complete_button.grid(row=2, column=1, padx=5, pady=5)

# Task listbox
task_list = tk.Listbox(root, width=50)
task_list.grid(row=1, column=0, padx=5, pady=5)

# Task count label
task_count_label = tk.Label(root, text="Total Tasks: 0")
task_count_label.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
