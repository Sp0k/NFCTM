import tkinter as tk
from interface import TaskManagerInterface
from db import DatabaseManager


def main():
    db = DatabaseManager()

    root = tk.Tk()
    app = TaskManagerInterface(root, db)

    root.mainloop()


if __name__ == "__main__":
    main()
