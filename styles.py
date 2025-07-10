from config import COLORS

CUSTOM_CSS = f"""
<style>
    .main-header {{
        background: linear-gradient(90deg, {COLORS['primary']}, {COLORS['secondary']});
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    
    .metric-card {{
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid {COLORS['primary']};
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    
    .metric-card h3 {{
        color: {COLORS['primary']};
        margin-top: 0;
    }}
    
    .metric-card h2 {{
        color: {COLORS['accent']};
        font-size: 1.5rem;
    }}
    
    @media (max-width: 768px) {{
        .main-header {{
            padding: 1rem;
        }}
        .metric-card {{
            padding: 0.5rem;
        }}
    }}

    .hideScrollbar .st-emotion-cache-79elbk{{
        display: none;
    }}
</style>
"""

def apply_custom_styles():
    from streamlit import markdown
    markdown(CUSTOM_CSS, unsafe_allow_html=True)