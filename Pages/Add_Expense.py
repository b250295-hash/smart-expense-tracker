import streamlit as st
from datetime import date

from models import expense
from config import CATEGORIES
from validators import validate_expense
from ui.components import render_sidebar_profile

render_sidebar_profile()

st.markdown("### ➕ Add Expense")
st.markdown("""<div style='color:#cbd5e1'>Record a new expense transaction quickly and easily.</div>""", unsafe_allow_html=True)

with st.form("expense_form", clear_on_submit=True):
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    
    expense_date = st.date_input("Date", value=date.today())
    category = st.selectbox("Category", CATEGORIES)
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0, format="%.2f")
    description = st.text_area("Description")

    st.markdown('</div>', unsafe_allow_html=True)
    
    submitted = st.form_submit_button("✅ Add Expense", use_container_width=True)

if submitted:

    valid, message = validate_expense(
        expense_date,
        category,
        amount,
        description
    )

    if valid:

        expense.add_expense(
            str(expense_date),
            category,
            amount,
            description
        )

        st.success("✅ Expense added successfully!")

    else:

        st.error(message)

st.divider()

st.subheader("📋 All Expenses")

expenses = expense.get_all_expenses()

if expenses:

    st.dataframe(
        expenses,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No expenses added yet.")