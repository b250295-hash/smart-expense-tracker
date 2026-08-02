import streamlit as st


def render_card(title: str, value: str, subtitle: str = "", icon: str = "") -> None:
    html = f"""
    <div class="card">
      <div style="display:flex; align-items:center; gap:12px;">
        <div style="font-size:1.6rem">{icon}</div>
        <div>
          <div class="title">{title}</div>
          <div class="value">{value}</div>
          <div style="color: #94a3b8; font-size:0.85rem; margin-top:6px;">{subtitle}</div>
        </div>
      </div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)


def render_clickable_card(icon: str, title: str, description: str, page_name: str) -> None:
    """Render a clickable card that navigates to a page."""
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    
    with col2:
        html = f"""
        <div class="clickable-card" style="cursor: pointer; border-radius: 12px; overflow: hidden;">
            <div style="background: linear-gradient(135deg, rgba(79,70,229,0.08), rgba(20,184,166,0.04)); border: 1px solid rgba(148, 163, 184, 0.22); padding: 1.5rem; border-radius: 12px; transition: all 0.3s ease; hover_bg: linear-gradient(135deg, rgba(79,70,229,0.15), rgba(20,184,166,0.1));">
                <div style="font-size: 2rem; margin-bottom: 0.75rem;">{icon}</div>
                <div style="font-size: 1.25rem; font-weight: 600; color: #f8fafc; margin-bottom: 0.5rem;">{title}</div>
                <div style="color: #cbd5e1; font-size: 0.95rem;">{description}</div>
            </div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)
        
        if st.button(f"Open {title}", key=f"btn_{page_name}", use_container_width=True, type="primary"):
            st.switch_page(f"pages/{page_name}.py")


def render_nav_cards() -> None:
    """Render the main navigation cards for the home page."""
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_clickable_card(
            "📊", 
            "Dashboard", 
            "View your expense summary.",
            "Dashboard"
        )
    
    with col2:
        render_clickable_card(
            "💰",
            "Budget",
            "Set and monitor your monthly budget.",
            "Budget"
        )
    
    with col3:
        render_clickable_card(
            "📈",
            "Analytics",
            "Visualize your spending with interactive charts.",
            "Analytics"
        )


def render_sidebar_profile() -> None:
    """Render a profile panel in the sidebar."""
    st.sidebar.markdown(
        """
        <div class="sidebar-profile">
            <div style="font-size:1.8rem; margin-bottom:0.5rem;">💰</div>
            <div style="font-weight:600; color:#f8fafc; font-size:1.1rem; margin-bottom:0.25rem;">Smart Tracker</div>
            <div style="color: #94a3b8; font-size:0.85rem;">Financial Dashboard</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.divider()


def render_info_banner(message: str, icon: str = "ℹ️") -> None:
    """Render an info banner with custom styling."""
    html = f"""
    <div style="background: rgba(79,70,229,0.1); border: 1px solid rgba(79,70,229,0.3); padding: 0.75rem; border-radius: 8px; color: #cbd5e1; font-size:0.95rem;">
        <span style="font-size:1.2rem; margin-right:0.5rem;">{icon}</span>{message}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
