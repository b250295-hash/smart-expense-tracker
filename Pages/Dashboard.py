
import streamlit as st

from models import expense
from budget import budget
from analytics import analytics
from charts import charts
from utils import format_currency
from ui.components import render_card


st.markdown("### 📊 Dashboard")
st.markdown("""<div style='color:#cbd5e1'>Overview of your finances, recent activity, and quick insights.</div>""", unsafe_allow_html=True)

expenses = expense.get_all_expenses()
total_expense = analytics.total_expense()
monthly_budget = budget.get_budget()
remaining_budget = budget.remaining_budget()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Expense",
        format_currency(total_expense)
    )

with col2:
    st.metric(
        "🎯 Monthly Budget",
        format_currency(monthly_budget)
    )

with col3:
    st.metric(
        "💵 Remaining Budget",
        format_currency(remaining_budget)
    )

st.divider()

# Top metrics rendered as cards
total_expense = analytics.total_expense()
monthly_budget = budget.get_budget()
remaining_budget = budget.remaining_budget()

col1, col2, col3 = st.columns(3)

with col1:
    render_card("Total Expense", format_currency(total_expense), "All time total", "💸")

with col2:
    render_card("Monthly Budget", format_currency(monthly_budget), "Set for current month", "🎯")

with col3:
    render_card("Remaining", format_currency(remaining_budget), "Left this month", "🔰")

st.divider()

st.subheader("📋 Recent Expenses")

if expenses:
    st.dataframe(
        expense.get_all_expenses(),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No expenses added yet.")

st.divider()

st.subheader("📈 Expense Analytics")

pie_chart = charts.category_pie_chart()

if pie_chart:
    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )
else:
    st.info("Add some expenses to view charts.")