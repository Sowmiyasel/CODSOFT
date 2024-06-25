import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the list
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to update the listbox with the current tasks
def update_task_list():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{index}. {task}")
        if index % 2 == 0:
            task_listbox.itemconfig(tk.END, {'bg':'#f0f0f0'})
        else:
            task_listbox.itemconfig(tk.END, {'bg':'#ffffff'})

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create the list to hold tasks
tasks = []

# Create and place widgets
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Selected Task", width=48, command=delete_task)
delete_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()