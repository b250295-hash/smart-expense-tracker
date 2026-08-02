import streamlit as st


def apply_theme() -> None:
    st.set_page_config(page_title="Smart Expense Tracker", page_icon="💸", layout="wide")

    st.markdown(
        """
        <style>
        :root {
            --primary-color: #4f46e5;
            --primary-dark: #312e81;
            --secondary-color: #14b8a6;
            --surface-color: #0f172a;
            --surface-soft: #111827;
            --text-color: #f8fafc;
            --muted-color: #94a3b8;
            --border-color: rgba(148, 163, 184, 0.22);
            --shadow-color: rgba(15, 23, 42, 0.35);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #020617 0%, #0f172a 45%, #111827 100%);
            color: var(--text-color);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.98), rgba(2, 6, 23, 0.98));
            border-right: 1px solid var(--border-color);
        }

        .stAppHeader {
            background: transparent;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1400px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc;
            letter-spacing: 0.01em;
        }

        .stMetric, .stAlert, .stDataFrame, .stTextInput, .stSelectbox, .stNumberInput, .stTextArea {
            border-radius: 16px;
        }

        .stMetric {
            background: rgba(15, 23, 42, 0.75);
            padding: 1rem;
            border: 1px solid var(--border-color);
            box-shadow: 0 12px 45px var(--shadow-color);
        }

        div[data-testid="stMetricLabel"] {
            color: var(--muted-color);
        }

        div[data-testid="stMetricValue"] {
            color: var(--text-color);
            font-weight: 700;
        }

        .stButton > button {
            border-radius: 999px;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }

        .stButton > button:hover {
            filter: brightness(1.08);
            box-shadow: 0 8px 18px rgba(20, 184, 166, 0.25);
        }

        .stDataFrame {
            border: 1px solid var(--border-color);
        }

        .stProgress > div > div {
            background: linear-gradient(90deg, var(--secondary-color), var(--primary-color));
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 999px;
            color: var(--muted-color);
        }

        .stTabs [data-baseweb="tab][aria-selected="true"] {
            background: rgba(79, 70, 229, 0.18);
            color: white;
        }
        /* Card styles */
        .card {
            background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
            border: 1px solid var(--border-color);
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 8px 30px rgba(2,6,23,0.45);
            margin-bottom: 1rem;
        }

        .card .title {
            color: var(--muted-color);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }

        .card .value {
            color: var(--text-color);
            font-size: 1.45rem;
            font-weight: 700;
        }

        .panel {
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border-color);
            padding: 1rem 1.25rem;
            border-radius: 12px;
        }

        .sidebar-profile {
            padding: 1rem;
            margin: 0.5rem 0 1rem 0;
            border-radius: 12px;
            background: linear-gradient(90deg, rgba(79,70,229,0.06), rgba(20,184,166,0.04));
            text-align: center;
        }

        .sidebar-profile img { width:64px; height:64px; border-radius:50%; }

        /* Clickable card styles */
        .clickable-card {
            transition: all 0.3s ease;
        }

        .clickable-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 40px rgba(20, 184, 166, 0.15);
        }

        .clickable-card > div {
            transition: all 0.3s ease;
        }

        .clickable-card:hover > div {
            background: linear-gradient(135deg, rgba(79,70,229,0.15), rgba(20,184,166,0.1));
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
