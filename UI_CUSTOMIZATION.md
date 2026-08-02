# UI Customization Guide

This project features a premium dark theme built with a modern card-based layout system. Customize colors, spacing, and styles easily.

## Theme Configuration

Edit `ui/theme_config.py` to customize the UI:

```python
THEME = {
    "colors": {
        "primary": "#4f46e5",      # Main action color (Indigo)
        "secondary": "#14b8a6",    # Accent color (Teal)
        "surface": "#0f172a",      # Main background
        "text": "#f8fafc",         # Text color (Light)
        "muted": "#94a3b8",        # Secondary text
    },
    # ... more settings
}
```

## UI Components

All reusable components are in `ui/components.py`:

### `render_card(title, value, subtitle, icon)`
Display a metric in a styled card:
```python
render_card("Total Expense", "$1,234.56", "All time", "💸")
```

### `render_sidebar_profile()`
Add a profile panel to the sidebar (automatically called on all pages).

### `render_info_banner(message, icon)`
Display a custom info/warning banner:
```python
render_info_banner("Budget exceeded!", "🚨")
```

### `render_nav_cards()`
Render clickable navigation cards for the home page (Dashboard, Budget, Analytics):
```python
render_nav_cards()  # Auto-generates three clickable cards
```

### `render_clickable_card(icon, title, description, page_name)`
Create a single clickable card that navigates to a page:
```python
render_clickable_card("📊", "Dashboard", "View your summary", "Dashboard")
```

## Theme System

- **`ui/theme.py`**: Core CSS and page configuration
- **`ui/theme_config.py`**: Centralized color/spacing configuration
- **`ui/components.py`**: Reusable UI helpers

All pages automatically inherit the theme through `apply_theme()` in `app.py`.

## Page Structure

Every page now follows this pattern:

```python
from ui.components import render_sidebar_profile, render_card

# 1. Add sidebar profile
render_sidebar_profile()

# 2. Add hero text
st.markdown("### 📊 Page Title")
st.markdown("""<div style='color:#cbd5e1'>Subtitle description.</div>""", unsafe_allow_html=True)

# 3. Use cards for metrics
render_card("Title", "Value", "Subtitle", "Icon")

# 4. Wrap content in panels
st.markdown('<div class="panel">', unsafe_allow_html=True)
# ... content ...
st.markdown('</div>', unsafe_allow_html=True)
```

## Color Palette

| Role | Color | Hex |
|------|-------|-----|
| Primary | Indigo | #4f46e5 |
| Secondary | Teal | #14b8a6 |
| Success | Green | #10b981 |
| Warning | Amber | #f59e0b |
| Error | Red | #ef4444 |
| Surface | Dark Blue | #0f172a |
| Text | Light Gray | #f8fafc |
| Muted | Gray | #94a3b8 |

## Running the App

```bash
streamlit run app.py
```

All pages (Dashboard, Analytics, Budget, Expenses, Reports) use the unified theme system.
