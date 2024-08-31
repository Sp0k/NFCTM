import sqlite3


class DatabaseManager:
    def __init__(self, db_name="task_manager.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tasks_table()

    def create_tasks_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    due_date DATE,
                    priority INTEGER,
                    description TEXT
                )
                """
            )

    def add_task(self, title, due_date, priority, description):
        with self.connection:
            self.connection.execute(
                "INSERT INTO tasks (title, due_date, priority, description) VALUES (?, ?, ?, ?)",
                (title, due_date, priority, description),
            )

    def get_tasks(self, order_by=None):
        cursor = self.connection.cursor()
        query = "SELECT * FROM tasks"
        if order_by:
            query += f" ORDER BY {order_by}"
        cursor.execute(query)
        return cursor.fetchall()

    def delete_all_tasks(self):
        with self.connection:
            self.connection.execute("DELETE FROM tasks")

    def __del__(self):
        self.connection.close()
