import pandas as pd
import plotly.graph_objects as go
from utils.charts import configure_layout

def create_comparison_table():
    """Cria tabela de comparação de modelos"""
    return pd.DataFrame({
        "Modelo": ["ARIMA", "SARIMA (Inicial)", "SARIMA (Ajustado)"],
        "RMSE": [1.7857, 5.4624, 2.4102],
        "MAE": [1.2345, 4.1234, 1.9876],
        "MAPE (%)": [5.67, 15.23, 7.89]
    })

def show_tab(vegetable):
    """Mostra a aba de comparação de modelos"""
    from streamlit import header, dataframe, plotly_chart
    
    header(f"Comparação de Modelos para {vegetable}")
    
    # Tabela de comparação
    comparison_df = create_comparison_table()
    styled_df = comparison_df.style.format({
        'RMSE': '{:.4f}', 
        'MAE': '{:.4f}', 
        'MAPE (%)': '{:.2f}'
    })
    
    dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Gráfico de comparação
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=comparison_df["Modelo"],
        y=comparison_df["RMSE"],
        name='RMSE',
        marker_color=['#D62728', '#1F77B4', '#FF7F0E'],
        text=comparison_df["RMSE"],
        texttemplate='%{text:.3f}',
        textposition='outside'
    ))
    
    fig.update_layout(
        configure_layout("Comparação de Erros (RMSE) entre Modelos"),
        xaxis_title="Modelo",
        yaxis_title="RMSE",
        showlegend=False
    )
    
    plotly_chart(fig, use_container_width=True)