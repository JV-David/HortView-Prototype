import plotly.graph_objects as go
from utils.charts import configure_layout, create_line_trace
import streamlit as st 

def show_tab(forecast_data, vegetable):
    """Mostra a aba do modelo ARIMA"""
    from streamlit import header, expander, plotly_chart
    
    header(f"Modelo ARIMA para {vegetable}")
    
    with expander("ℹ️ Sobre o Modelo ARIMA"):
        st.write("""
        O modelo ARIMA (AutoRegressive Integrated Moving Average) é usado para:
        - Previsão de séries temporais
        - Modelar relações entre observações e defasagens
        - Considerar diferenciação e médias móveis
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
        forecast_data["ARIMA"], 
        'Previsões ARIMA', 
        '#D62728',
        'dot'
    ))
    
    fig.update_layout(configure_layout("Previsões ARIMA"))
    plotly_chart(fig, use_container_width=True)