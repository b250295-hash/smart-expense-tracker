import sqlite3


class Database:
    def __init__(self, db_name="expense_tracker.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS budget(
                id INTEGER PRIMARY KEY,
                monthly_budget REAL
            )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()


db = Database()