import streamlit as st
import pandas as pd

from models import expense
from utils import export_to_csv, format_currency
from ui.components import render_card, render_sidebar_profile

render_sidebar_profile()

st.markdown("### 📋 Expense Reports")
st.markdown("""<div style='color:#cbd5e1'>View detailed reports and export your expense data.</div>""", unsafe_allow_html=True)

expenses = expense.get_all_expenses()

if not expenses:
    st.info("No expense records found.")
    st.stop()

df = pd.DataFrame(
    expenses,
    columns=[
        "ID",
        "Date",
        "Category",
        "Amount",
        "Description"
    ]
)

st.subheader("All Expense Records")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    render_card("Total Expenses", format_currency(df["Amount"].sum()), "All time", "💰")

with col2:
    render_card("Total Transactions", str(len(df)), "Records", "📊")

st.divider()

st.subheader("Category-wise Summary")

summary = (
    df.groupby("Category")["Amount"]
      .sum()
      .reset_index()
      .sort_values(by="Amount", ascending=False)
)

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

csv = export_to_csv()

if csv:
    st.download_button(
        label="📥 Download Report (CSV)",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )