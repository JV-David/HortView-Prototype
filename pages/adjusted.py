import plotly.graph_objects as go
from utils.charts import configure_layout, create_line_trace
import streamlit as st 

def show_tab(forecast_data, vegetable):
    """Mostra a aba do SARIMA ajustado"""
    from streamlit import header, expander, plotly_chart
    
    header(f"Modelo SARIMA Ajustado para {vegetable}")
    
    with expander("ℹ️ Sobre o Modelo SARIMA Ajustado"):
        st.write("""
        O modelo SARIMA Ajustado apresenta:
        - Parâmetros otimizados
        - Possível transformação nos dados
        - Melhor ajuste que o SARIMA inicial
        - Menor erro de previsão
        """)
    
    fig = go.Figure()
    fig.add_trace(create_line_trace(
        forecast_data.index, 
        forecast_data["Dados Reais"], 
        'Dados Reais', 
        '#2E8B57'
    ))
    fig.add_trace(create_line_trace(
        forecast_data.index, 
        forecast_data["SARIMA"], 
        'Previsões SARIMA Ajustado', 
        '#FF7F0E',
        'dot'
    ))
    
    fig.update_layout(configure_layout("Previsões SARIMA Ajustado"))
    plotly_chart(fig, use_container_width=True)