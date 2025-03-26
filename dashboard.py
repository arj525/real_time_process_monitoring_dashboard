import psutil
import tkinter as tk
from tkinter import ttk

class ProcessMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Process Monitoring Dashboard")
        self.root.geometry("800x400")

        # Setting up the treeview
        self.tree = ttk.Treeview(root, columns=("PID", "Name", "CPU", "Memory"), show="headings")
        self.tree.heading("PID", text="PID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("CPU", text="CPU (%)")
        self.tree.heading("Memory", text="Memory (MB)")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Refresh data every second
        self.update_processes()

    def update_processes(self):
        # Clear previous data
        for row in self.tree.get_children():
                self.tree.delete(row)

        # Fetch and display process data
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                cpu = proc.info['cpu_percent']
                memory = proc.info['memory_info'].rss / (1024 * 1024)  # Convert to MB
                self.tree.insert("", "end", values=(pid, name, cpu, round(memory, 2)))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        # Schedule next update
        self.root.after(1000, self.update_processes)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessMonitor(root)
    root.mainloop()
