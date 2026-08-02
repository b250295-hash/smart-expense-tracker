from database import db


class Budget:
    def set_budget(self, monthly_budget):
        db.cursor.execute("SELECT * FROM budget WHERE id = 1")
        data = db.cursor.fetchone()

        if data:
            db.cursor.execute("""
                UPDATE budget
                SET monthly_budget = ?
                WHERE id = 1
            """, (monthly_budget,))
        else:
            db.cursor.execute("""
                INSERT INTO budget(id, monthly_budget)
                VALUES(1, ?)
            """, (monthly_budget,))

        db.conn.commit()

    def get_budget(self):
        db.cursor.execute("""
            SELECT monthly_budget
            FROM budget
            WHERE id = 1
        """)
        data = db.cursor.fetchone()

        if data:
            return data[0]
        return 0

    def remaining_budget(self):
        budget = self.get_budget()

        db.cursor.execute("""
            SELECT SUM(amount)
            FROM expenses
        """)
        total = db.cursor.fetchone()[0]

        if total is None:
            total = 0

        return budget - total

    def total_expense(self):
        db.cursor.execute("""
            SELECT SUM(amount)
            FROM expenses
        """)
        total = db.cursor.fetchone()[0]

        if total is None:
            return 0

        return total


budget = Budget()