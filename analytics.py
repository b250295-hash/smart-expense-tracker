from database import db
import pandas as pd


class Analytics:

    def get_dataframe(self):
        query = """
            SELECT date, category, amount, description
            FROM expenses
            ORDER BY date DESC
        """
        df = pd.read_sql_query(query, db.conn)
        return df

    def total_expense(self):
        df = self.get_dataframe()

        if df.empty:
            return 0

        return df["amount"].sum()

    def category_summary(self):
        df = self.get_dataframe()

        if df.empty:
            return pd.DataFrame(columns=["category", "amount"])

        return (
            df.groupby("category", as_index=False)["amount"]
            .sum()
            .sort_values(by="amount", ascending=False)
        )

    def monthly_summary(self):
        df = self.get_dataframe()

        if df.empty:
            return pd.DataFrame(columns=["Month", "Amount"])

        df["date"] = pd.to_datetime(df["date"])
        df["Month"] = df["date"].dt.strftime("%b %Y")

        return (
            df.groupby("Month", as_index=False)["amount"]
            .sum()
        )

    def highest_expense(self):
        df = self.get_dataframe()

        if df.empty:
            return None

        return df.loc[df["amount"].idxmax()]

    def lowest_expense(self):
        df = self.get_dataframe()

        if df.empty:
            return None

        return df.loc[df["amount"].idxmin()]


analytics = Analytics()