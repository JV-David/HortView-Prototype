import plotly.graph_objects as go
from utils.charts import configure_layout, create_line_trace
import streamlit as st 

def show_tab(forecast_data, vegetable):
    """Mostra a aba do modelo SARIMA"""
    from streamlit import header, expander, plotly_chart
    
    header(f"Modelo SARIMA para {vegetable}")
    
    with expander("ℹ️ Sobre o Modelo SARIMA"):
        st.write("""
        O modelo SARIMA (Seasonal ARIMA) inclui:
        - Componentes sazonais explícitas
        - Parâmetros adicionais para sazonalidade (P,D,Q,m)
        - Melhor desempenho em dados com padrões sazonais
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
        'Previsões SARIMA', 
        '#1F77B4',
        'dot'
    ))
    
    fig.update_layout(configure_layout("Previsões SARIMA"))
    plotly_chart(fig, use_container_width=True)