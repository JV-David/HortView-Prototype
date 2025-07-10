import plotly.graph_objects as go
from utils.charts import configure_layout, create_line_trace
from components.metrics import show_price_metrics

def show_tab(price_data, vegetable):
    """Mostra a aba do gráfico original"""
    from streamlit import header
    
    header(f"Evolução dos Preços da {vegetable}")
    show_price_metrics(price_data)
    
    fig = go.Figure()
    fig.add_trace(create_line_trace(
        price_data.index, 
        price_data['Preço'], 
        'Preço', 
        '#2E8B57'
    ))
    fig.update_layout(configure_layout(f"Evolução dos Preços da {vegetable}"))
    
    from streamlit import plotly_chart
    plotly_chart(fig, use_container_width=True)