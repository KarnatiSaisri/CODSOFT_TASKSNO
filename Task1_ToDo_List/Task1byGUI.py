import sqlite3
import tkinter as tk
from tkinter import messagebox


# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_text TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# --- GUI APPLICATION ---
class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("400x450")

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=25, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        add_btn = tk.Button(
            input_frame, text="Add", width=8, command=self.add_task
        )
        add_btn.pack(side=tk.LEFT)

        # Listbox for Tasks
        self.task_listbox = tk.Listbox(
            root, width=35, height=15, font=("Arial", 12)
        )
        self.task_listbox.pack(pady=10)

        # Action Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        update_btn = tk.Button(
            btn_frame, text="Update Selected", width=15, command=self.update_task
        )
        update_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = tk.Button(
            btn_frame, text="Delete Selected", width=15, command=self.delete_task
        )
        delete_btn.pack(side=tk.LEFT, padx=5)

        # Load initial data
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("SELECT task_text FROM tasks")
        for row in cursor.fetchall():
            self.task_listbox.insert(tk.END, row[0])
        conn.close()

    def add_task(self):
        text = self.task_entry.get().strip()
        if text:
            conn = sqlite3.connect("todo.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task_text) VALUES (?)", (text,))
            conn.commit()
            conn.close()
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            old_text = self.task_listbox.get(selected_index)
            new_text = self.task_entry.get().strip()

            if new_text:
                conn = sqlite3.connect("todo.db")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE tasks SET task_text = ? WHERE task_text = ?",
                    (new_text, old_text),
                )
                conn.commit()
                conn.close()
                self.task_entry.delete(0, tk.END)
                self.load_tasks()
            else:
                messagebox.showwarning(
                    "Warning", "Type the new text in the input box first!"
                )
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to update!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            text = self.task_listbox.get(selected_index)

            conn = sqlite3.connect("todo.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE task_text = ?", (text,))
            conn.commit()
            conn.close()
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete!")


if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
