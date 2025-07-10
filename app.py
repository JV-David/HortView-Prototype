import streamlit as st
from config import PAGE_CONFIG
from styles import apply_custom_styles
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
from utils.data_loader import load_data, prepare_data
from pages import original, seasonal, arima, sarima, adjusted, comparison

def main():
    # Configuração inicial
    st.set_page_config(**PAGE_CONFIG)
    apply_custom_styles()
    
    # Carregar dados
    prices, forecasts_02, forecasts_04 = load_data()
    vegetables = prices['Designacao'].unique()
    
    # Componentes da UI
    show_header()
    selected_vegetable = show_sidebar(vegetables)
    
    # Preparar dados
    data = prepare_data(prices, forecasts_02, forecasts_04, selected_vegetable)
    
    # Verificar dados
    if data["forecast_02"] is None or data["forecast_04"] is None:
        st.error(f"Dados de previsão para {selected_vegetable} não encontrados!")
        st.stop()
    
    # Criar abas
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Original", "🔄 Sazonalidade", 
        "📊 ARIMA", "📈 SARIMA", 
        "🔄 SARIMA Ajustado", "🔍 Comparação"
    ])
    
    # Mostrar cada aba
    with tab1:
        original.show_tab(data["price_data"], selected_vegetable)
    
    with tab2:
        seasonal.show_tab(data["price_data"], selected_vegetable)
    
    with tab3:
        arima.show_tab(data["forecast_02"], selected_vegetable)
    
    with tab4:
        sarima.show_tab(data["forecast_02"], selected_vegetable)
    
    with tab5:
        adjusted.show_tab(data["forecast_04"], selected_vegetable)
    
    with tab6:
        comparison.show_tab(selected_vegetable) 
    
    # ... outras abas
    
    show_footer()

if __name__ == "__main__":
    main()