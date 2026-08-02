
import streamlit as st

from analytics import analytics
from charts import charts
from utils import format_currency
from ui.components import render_card

st.markdown("### 📈 Expense Analytics")
st.markdown("""<div style='color:#cbd5e1'>Interactive charts and summaries to help you understand spending trends.</div>""", unsafe_allow_html=True)

# Total Expense
total = analytics.total_expense()

st.metric(
    "💰 Total Expense",
    format_currency(total)
)

st.divider()

# Highest & Lowest Expense
col1, col2 = st.columns(2)

highest = analytics.highest_expense()
lowest = analytics.lowest_expense()

with col1:
    st.subheader("🔺 Highest Expense")

    if highest is not None:
        st.write(f"**Category:** {highest['category']}")
        st.write(f"**Amount:** {format_currency(highest['amount'])}")
        st.write(f"**Date:** {highest['date']}")
    else:
        st.info("No expense data available.")

with col2:
    st.subheader("🔻 Lowest Expense")

    if lowest is not None:
        st.write(f"**Category:** {lowest['category']}")
        st.write(f"**Amount:** {format_currency(lowest['amount'])}")
        st.write(f"**Date:** {lowest['date']}")
    else:
        st.info("No expense data available.")

st.divider()

st.subheader("🥧 Category-wise Expense Distribution")

pie_chart = charts.category_pie_chart()

if pie_chart:
    with st.container():
        st.markdown('<div class="card"><div class="title">Category Distribution</div>', unsafe_allow_html=True)
        st.plotly_chart(pie_chart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No data available.")

st.divider()

st.subheader("📊 Category-wise Expenses")

bar_chart = charts.category_bar_chart()

if bar_chart:
    with st.container():
        st.markdown('<div class="card"><div class="title">Category-wise Expenses</div>', unsafe_allow_html=True)
        st.plotly_chart(bar_chart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.subheader("📈 Monthly Expense Trend")

line_chart = charts.monthly_line_chart()

if line_chart:
    with st.container():
        st.markdown('<div class="card"><div class="title">Monthly Trend</div>', unsafe_allow_html=True)
        st.plotly_chart(line_chart, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)