import streamlit as st
from ui import apply_theme
from ui.components import render_sidebar_profile, render_nav_cards
from config import APP_TITLE

# Apply global theme (page config + CSS)
apply_theme()
render_sidebar_profile()

st.header(APP_TITLE)

st.markdown("---")

st.subheader("Welcome — Smart, beautiful expense tracking")

st.write(
    "Manage your daily expenses, set monthly budgets, analyze spending patterns, and export reports — with a clean, modern UI."
)

render_nav_cards()

st.markdown("---")

st.write("Use the sidebar to navigate through pages.")

st.sidebar.success("Select a page")