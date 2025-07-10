import plotly.graph_objects as go
from config import COLORS

def configure_layout(title):
    """Configura layout padrão para gráficos"""
    return dict(
        title=title,
        xaxis_title="Tempo",
        yaxis_title="Preço (Meticais)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor='black'
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            linecolor='black',
            gridcolor='rgba(211,211,211,0.3)'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=50, r=50, b=50, t=80),
        hovermode="x unified"
    )

def create_line_trace(x, y, name, color, dash=None):
    """Cria um trace de linha padrão"""
    return go.Scatter(
        x=x, y=y,
        mode='lines+markers',
        line=dict(color=color, width=2, dash=dash),
        marker=dict(size=5),
        name=name,
        hovertemplate=f'<b>%{{x|%b %Y}}</b><br>{name}: %{{y:.2f}} MZN<extra></extra>'
    )