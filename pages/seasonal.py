from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.graph_objects as go
from utils.charts import configure_layout, create_line_trace
import streamlit as st 

def show_tab(price_data, vegetable):
    """Mostra a aba de análise sazonal"""
    from streamlit import header, expander, plotly_chart
    
    header(f"Decomposição Sazonal da {vegetable}")
    
    with expander("ℹ️ Sobre a Análise de Sazonalidade"):
        st.write("""
        A decomposição sazonal separa a série temporal em componentes:
        - Observado: Dados originais
        - Tendência: Direção geral dos dados
        - Sazonalidade: Padrões repetitivos
        - Resíduos: O que resta após remover tendência e sazonalidade
        """)
    
    decomposition = seasonal_decompose(price_data['Preço'], model="additive", period=12)
    
    fig = go.Figure()
    fig.add_trace(create_line_trace(
        decomposition.observed.index, 
        decomposition.observed, 
        'Observado', 
        '#2E8B57'
    ))
    fig.add_trace(create_line_trace(
        decomposition.trend.index, 
        decomposition.trend, 
        'Tendência', 
        '#FF7F0E'
    ))
    fig.add_trace(create_line_trace(
        decomposition.seasonal.index, 
        decomposition.seasonal, 
        'Sazonalidade', 
        '#1F77B4'
    ))
    fig.add_trace(create_line_trace(
        decomposition.resid.index, 
        decomposition.resid, 
        'Resíduos', 
        '#D62728'
    ))
    
    fig.update_layout(configure_layout("Decomposição Sazonal"))
    plotly_chart(fig, use_container_width=True)