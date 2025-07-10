import pandas as pd
from config import DATA_PATHS

def load_data():
    """Carrega todos os datasets necessários"""
    prices = pd.read_excel(DATA_PATHS["prices"], sheet_name="Preparados")
    forecasts_02 = pd.read_excel(DATA_PATHS["forecasts_02"], sheet_name=None)
    forecasts_04 = pd.read_excel(DATA_PATHS["forecasts_04"], sheet_name=None)
    return prices, forecasts_02, forecasts_04

def prepare_data(prices, forecasts_02, forecasts_04, selected_vegetable):
    """Prepara os dados para a hortaliça selecionada"""
    # Filtrar dados de preços
    price_data = prices[prices['Designacao'] == selected_vegetable].drop(columns=['Designacao']).T
    price_data.columns = ['Preço']
    price_data.index = pd.to_datetime(price_data.index, format='%b.%y', errors='coerce')
    
    # Preparar dados de previsão
    def prepare_forecast(forecast_data, vegetable):
        if vegetable in forecast_data:
            df = forecast_data[vegetable].copy()
            df['Meses'] = pd.to_datetime(df['Meses'], format='%b/%y', errors='coerce')
            df.set_index('Meses', inplace=True)
            return df
        return None
    
    forecast_02 = prepare_forecast(forecasts_02, selected_vegetable)
    forecast_04 = prepare_forecast(forecasts_04, selected_vegetable)
    
    return {
        "price_data": price_data,
        "forecast_02": forecast_02,
        "forecast_04": forecast_04
    }