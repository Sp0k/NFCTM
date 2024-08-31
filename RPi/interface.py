import tkinter as tk
from tkinter import Canvas
from datetime import datetime


class TaskManagerInterface:
    def __init__(self, root):
        self.root = root
        self.setup_interface()

    def setup_interface(self):
        # Setup window
        self.root.geometry("800x480")
        self.root.configure(bg="#010209")

        # Setup interface parts
        self.setup_footer()
        self.setup_sidebar()

        # Make the window borderless
        self.root.overrideredirect(True)

        # Start the time and date updates
        self.footer_data()

    def time(self):
        # Get and display current time
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.config(text=current_time, font=("Source Sans Pro", 27))
        self.time_label.after(1000, self.time)

    def date(self):
        # Get and display current date
        current_date = datetime.now().strftime("%a. %b %d %Y")
        self.date_label.config(text=current_date, font=("Source Sans Pro", 17))
        self.date_label.after(1000, self.date)

    def footer_data(self):
        self.time()
        self.date()

    def setup_footer(self):
        # Create a time and date footer
        footer = tk.Frame(self.root, bg="#010209")
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=15)

        # Footer separation line
        bottom_line = Canvas(
            footer,
            width=765,
            height=0.3,
            bg="#475569",
            highlightthickness=0,
        )
        bottom_line.pack(fill=tk.Y)

        # Footer's labels
        self.date_label = tk.Label(footer, fg="#D9D9D9", bg="#010209")
        self.date_label.pack(side=tk.LEFT, padx=10)

        self.time_label = tk.Label(footer, fg="#D9D9D9", bg="#010209")
        self.time_label.pack(side=tk.RIGHT, padx=10)

    def setup_sidebar(self):
        # Sidebar Frame
        sidebar = tk.Frame(self.root, bg="#010209", width=150)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=7)

        # Sidebar label
        order_label = tk.Label(
            sidebar,
            bg="#010209",
            fg="#D9D9D9",
            text="Order by:",
            font=("Nunito Sans", 20, "underline"),
            pady=4,
        )

        # Sidebar Buttons
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
        )

        # Temp Buttons
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
        )

        # Sidebar line
        side_line = Canvas(
            sidebar,
            width=0.3,
            height=399,
            bg="#475569",
            highlightthickness=0,
        )

        # Sidebar pack
        side_line.pack(side=tk.RIGHT, padx=12)
        order_label.pack(fill=tk.X, pady=5)
        btn_due_date.pack(fill=tk.X, pady=5)
        btn_priority.pack(fill=tk.X, pady=5)
        btn_new_test.pack(fill=tk.X, pady=55)
        btn_close.pack(fill=tk.X)
