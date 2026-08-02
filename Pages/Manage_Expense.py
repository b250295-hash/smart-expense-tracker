import streamlit as st
import pandas as pd

from models import expense
from config import CATEGORIES
from ui.components import render_sidebar_profile

render_sidebar_profile()

st.markdown("### ✏️ Manage Expenses")
st.markdown("""<div style='color:#cbd5e1'>Edit or delete existing expense records.</div>""", unsafe_allow_html=True)

data = expense.get_all_expenses()

if not data:
    st.info("No expenses available.")
    st.stop()

df = pd.DataFrame(
    data,
    columns=[
        "ID",
        "Date",
        "Category",
        "Amount",
        "Description"
    ]
)

selected_id = st.selectbox(
    "Select Expense ID",
    df["ID"]
)

record = df[df["ID"] == selected_id].iloc[0]

with st.form("update_form"):
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    
    expense_date = st.text_input("Date", value=record["Date"])
    category = st.selectbox("Category", CATEGORIES, index=CATEGORIES.index(record["Category"]) if record["Category"] in CATEGORIES else 0)
    amount = st.number_input("Amount", min_value=0.0, value=float(record["Amount"]))
    description = st.text_area("Description", value=record["Description"])

    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        update = st.form_submit_button("✅ Update", use_container_width=True)
    with col2:
        delete = st.form_submit_button("🗑 Delete", use_container_width=True)

if update:

    expense.update_expense(
        selected_id,
        expense_date,
        category,
        amount,
        description
    )

    st.success("Expense updated successfully!")
    st.rerun()

if delete:

    expense.delete_expense(selected_id)

    st.success("Expense deleted successfully!")
    st.rerun()

st.divider()

st.subheader("📋 Expense Records")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)