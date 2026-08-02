import streamlit as st

from budget import budget
from utils import format_currency
from ui.components import render_card, render_sidebar_profile, render_info_banner

render_sidebar_profile()

st.markdown("### 💰 Budget Management")
st.markdown("""<div style='color:#cbd5e1'>Set and monitor your monthly budget allocation.</div>""", unsafe_allow_html=True)

current_budget = budget.get_budget()
total_expense = budget.total_expense()
remaining_budget = budget.remaining_budget()

st.subheader("Set Monthly Budget")

with st.container():
    st.markdown('<div class="panel" style="padding: 1.25rem;">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        new_budget = st.number_input(
            "Monthly Budget (₹)",
            min_value=0.0,
            value=float(current_budget),
            step=100.0
        )
    with col2:
        if st.button("💾 Save", use_container_width=True):
            budget.set_budget(new_budget)
            st.success("Budget updated!")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    render_card("Monthly Budget", format_currency(current_budget), "Target", "🎯")

with col2:
    render_card("Total Expenses", format_currency(total_expense), "Spent", "💸")

with col3:
    render_card("Remaining", format_currency(remaining_budget), "Available", "✨")

st.divider()

if current_budget == 0:
    render_info_banner("Please set your monthly budget to track spending.", "🎯")
else:
    percentage = (total_expense / current_budget) * 100
    percentage = min(percentage, 100)

    st.subheader("Budget Usage")

    st.progress(percentage / 100)

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Budget Used:** {percentage:.2f}%")
    with col2:
        st.write(f"**Remaining Days:** ~{max(0, int(30 - (percentage/100)*30))} days")

    st.divider()

    if total_expense > current_budget:
        render_info_banner("⚠️ You have exceeded your monthly budget!", "🚨")
    elif percentage >= 80:
        render_info_banner("You have used more than 80% of your budget.", "⚠️")
    else:
        render_info_banner("Your spending is within the budget.", "✅")