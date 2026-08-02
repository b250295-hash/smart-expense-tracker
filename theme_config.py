# UI Theme Configuration
# Customize colors, spacing, and appearance settings here

THEME = {
    "colors": {
        "primary": "#4f46e5",  # Indigo
        "primary_dark": "#312e81",
        "secondary": "#14b8a6",  # Teal
        "surface": "#0f172a",  # Dark blue
        "surface_soft": "#111827",
        "text": "#f8fafc",  # Light gray
        "muted": "#94a3b8",  # Medium gray
        "border": "rgba(148, 163, 184, 0.22)",
        "shadow": "rgba(15, 23, 42, 0.35)",
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444",
    },
    "spacing": {
        "xs": "0.25rem",
        "sm": "0.5rem",
        "md": "1rem",
        "lg": "1.5rem",
        "xl": "2rem",
    },
    "border_radius": {
        "sm": "8px",
        "md": "12px",
        "lg": "16px",
        "full": "999px",
    },
    "typography": {
        "font_size_sm": "0.85rem",
        "font_size_md": "0.95rem",
        "font_size_lg": "1.1rem",
        "font_weight_normal": "400",
        "font_weight_semibold": "600",
        "font_weight_bold": "700",
    },
}


def get_color(key: str) -> str:
    """Get a color from the theme."""
    keys = key.split(".")
    value = THEME["colors"]
    for k in keys:
        value = value[k]
    return value


def get_css_variables() -> str:
    """Generate CSS variables from theme config."""
    colors = THEME["colors"]
    css = ":root {\n"
    for name, value in colors.items():
        css += f"    --{name.replace('_', '-')}: {value};\n"
    css += "}\n"
    return css
