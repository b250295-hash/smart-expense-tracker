from database import db


class Expense:
    def add_expense(self, date, category, amount, description):
        db.cursor.execute("""
            INSERT INTO expenses(date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))
        db.conn.commit()

    def get_all_expenses(self):
        db.cursor.execute("""
            SELECT * FROM expenses
            ORDER BY date DESC
        """)
        return db.cursor.fetchall()

    def update_expense(self, expense_id, date, category, amount, description):
        db.cursor.execute("""
            UPDATE expenses
            SET date=?, category=?, amount=?, description=?
            WHERE id=?
        """, (date, category, amount, description, expense_id))
        db.conn.commit()

    def delete_expense(self, expense_id):
        db.cursor.execute("""
            DELETE FROM expenses
            WHERE id=?
        """, (expense_id,))
        db.conn.commit()

    def search_expenses(self, keyword):
        db.cursor.execute("""
            SELECT * FROM expenses
            WHERE category LIKE ?
               OR description LIKE ?
            ORDER BY date DESC
        """, (f"%{keyword}%", f"%{keyword}%"))
        return db.cursor.fetchall()


expense = Expense()