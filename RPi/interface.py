import tkinter as tk
from tkinter import Canvas, Checkbutton, Frame
from datetime import datetime, timedelta
import random


class TaskManagerInterface:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.setup_interface()
        self.setup_task_list()

    def setup_interface(self):
        self.root.geometry("800x480")
        self.root.configure(bg="#010209")

        self.setup_footer()
        self.setup_sidebar()

        # Make the window borderless
        self.root.overrideredirect(True)

        # Start the time and date updates
        self.footer_data()

    def time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.config(text=current_time, font=("Source Sans Pro", 27))
        self.time_label.after(1000, self.time)

    def date(self):
        current_date = datetime.now().strftime("%a. %b %d %Y")
        self.date_label.config(text=current_date, font=("Source Sans Pro", 17))
        self.date_label.after(1000, self.date)

    def footer_data(self):
        self.time()
        self.date()

    def setup_footer(self):
        footer = tk.Frame(self.root, bg="#010209")
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=15)

        bottom_line = Canvas(
            footer,
            width=765,
            height=0.3,
            bg="#475569",
            highlightthickness=0,
        )
        bottom_line.pack(fill=tk.Y)

        self.date_label = tk.Label(footer, fg="#D9D9D9", bg="#010209")
        self.date_label.pack(side=tk.LEFT, padx=10)

        self.time_label = tk.Label(footer, fg="#D9D9D9", bg="#010209")
        self.time_label.pack(side=tk.RIGHT, padx=10)

    def setup_sidebar(self):
        sidebar = tk.Frame(self.root, bg="#010209", width=150)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=7)

        order_label = tk.Label(
            sidebar,
            bg="#010209",
            fg="#D9D9D9",
            text="Order by:",
            font=("Nunito Sans", 20, "underline"),
            pady=4,
        )

        btn_due_date = tk.Button(
            sidebar,
            text="Due Date",
            bg="#010209",
            fg="#D9D9D9",
            padx=2,
            pady=4,
            font=("Nunito Sans", 18),
            activebackground="#010209",
            activeforeground="#FFFFFF",
            command=self.sort_by_due_date,
        )

        btn_priority = tk.Button(
            sidebar,
            text="Priority",
            bg="#010209",
            fg="#D9D9D9",
            padx=2,
            pady=4,
            font=("Nunito Sans", 18),
            activebackground="#010209",
            activeforeground="#FFFFFF",
            command=self.sort_by_priority,
        )

        btn_new_test = tk.Button(
            sidebar,
            text="New Test",
            bg="#010209",
            fg="#D9D9D9",
            padx=2,
            pady=4,
            font=("Nunito Sans", 18),
            activebackground="#010209",
            activeforeground="#FFFFFF",
            command=self.add_test_tasks,
        )

        btn_delete_all = tk.Button(
            sidebar,
            text="Delete All",
            bg="#d9534f",
            fg="#FFFFFF",
            padx=2,
            pady=4,
            font=("Nunito Sans", 18),
            activebackground="#d9534f",
            activeforeground="#FFFFFF",
            command=self.delete_all_tasks,
        )

        btn_close = tk.Button(
            sidebar,
            text="Close",
            bg="#010209",
            fg="#D9D9D9",
            padx=2,
            pady=4,
            font=("Nunito Sans", 18),
            activebackground="#010209",
            activeforeground="#FFFFFF",
            command=self.root.destroy,
        )

        side_line = Canvas(
            sidebar,
            width=0.3,
            height=399,
            bg="#475569",
            highlightthickness=0,
        )

        side_line.pack(side=tk.RIGHT, padx=12)
        order_label.pack(fill=tk.X, pady=5)
        btn_due_date.pack(fill=tk.X, pady=5)
        btn_priority.pack(fill=tk.X, pady=5)
        btn_new_test.pack(fill=tk.X, pady=20)
        btn_delete_all.pack(fill=tk.X, pady=5)
        btn_close.pack(fill=tk.X)

    def setup_task_list(self):
        # Create a canvas to act as a viewport
        self.canvas = Canvas(self.root, bg="#010209", highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a frame inside the canvas to hold the tasks
        self.tasks_frame = Frame(self.canvas, bg="#010209")
        self.tasks_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        # Create a window in the canvas to hold the tasks_frame
        self.canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        # Bind the mouse wheel event to scroll the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        # Bind touch events for scrolling
        self.canvas.bind("<ButtonPress-1>", self.start_scroll)
        self.canvas.bind("<B1-Motion>", self.on_scroll)

        # Bind scroll events directly to the task labels
        self.tasks_frame.bind_all("<ButtonPress-1>", self.start_scroll)
        self.tasks_frame.bind_all("<B1-Motion>", self.on_scroll)

        # Configure canvas to only scroll vertically
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), xscrollcommand=lambda *args: None
        )

        # Display initial tasks
        self.display_tasks(self.db.get_tasks())

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def start_scroll(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def on_scroll(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def display_tasks(self, tasks):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for task in tasks:
            task_frame = tk.Frame(self.tasks_frame, bg="#010209")
            task_frame.pack(fill=tk.X, pady=5)

            # Checkbutton to mark the task as completed
            completed_var = tk.BooleanVar()
            check_button = tk.Checkbutton(
                task_frame,
                variable=completed_var,
                command=lambda task_id=task[0]: self.complete_task(task_id),
                bg="#010209",
                fg="#D9D9D9",
                selectcolor="#d9534f",
            )
            check_button.pack(side=tk.LEFT, padx=10)

            # Task title in the middle
            task_title = tk.Label(
                task_frame,
                text=task[1],
                bg="#010209",
                fg="#D9D9D9",
                font=("Nunito Sans", 18),
                anchor="w",
            )
            task_title.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)

            # Due date on the right
            formatted_date = datetime.strptime(task[2], "%Y-%m-%d").strftime("%b. %d")
            due_date_label = tk.Label(
                task_frame,
                text=formatted_date,
                bg="#010209",
                fg="#D9D9D9",
                font=("Nunito Sans", 18),
                anchor="e",
            )
            due_date_label.pack(side=tk.RIGHT, padx=10)

    def complete_task(self, task_id):
        if isinstance(task_id, int):
            self.db.delete_task(task_id)
            self.display_tasks(self.db.get_tasks())
        else:
            print("Invalid task_id:", task_id)

    def sort_by_due_date(self):
        tasks = self.db.get_tasks(order_by="due_date ASC")
        self.display_tasks(tasks)

    def sort_by_priority(self):
        tasks = self.db.get_tasks(order_by="priority DESC")
        self.display_tasks(tasks)

    def add_test_tasks(self):
        priorities = [0, 1, 2, 3]
        for priority in priorities:
            task_title = f"Test Task Priority {priority}"
            random_days = random.randint(0, 30)
            due_date = (datetime.now() + timedelta(days=random_days)).date()
            self.db.add_task(task_title, due_date, priority, "")

        self.display_tasks(self.db.get_tasks())

    def delete_all_tasks(self):
        self.db.delete_all_tasks()
        self.display_tasks([])  # Clear the display
