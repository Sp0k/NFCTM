import tkinter as tk
from interface import TaskManagerInterface


def main():
    root = tk.Tk()
    app = TaskManagerInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
