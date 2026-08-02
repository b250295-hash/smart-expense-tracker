import pandas as pd
from models import expense


def get_expense_dataframe():
    """
    Returns all expenses as a Pandas DataFrame.
    """
    data = expense.get_all_expenses()

    columns = [
        "ID",
        "Date",
        "Category",
        "Amount",
        "Description"
    ]

    return pd.DataFrame(data, columns=columns)


def format_currency(amount):
    """
    Format amount with Indian Rupee symbol.
    """
    return f"₹{amount:,.2f}"


def export_to_csv():
    """
    Export all expenses to CSV.
    """
    df = get_expense_dataframe()

    if df.empty:
        return None

    return df.to_csv(index=False).encode("utf-8")


def total_expense():
    """
    Returns total expense.
    """
    df = get_expense_dataframe()

    if df.empty:
        return 0

    return df["Amount"].sum()