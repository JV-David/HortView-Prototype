import pandas as pd 
import numpy as np 
from sklearn.metrics import mean_squared_error 
import matplotlib.pyplot as plt 
from statsmodels.tsa.arima.model import ARIMA 
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_excel('Precos-Medio-Nampula-Cidade-2019-2024.xlsx', sheet_name='Preparados') 
 
#Transpor os dados para ter a data como índice 
df = df.set_index('Designacao').T.reset_index() 
 
#Corrigir o formato da data 
df['index'] = pd.to_datetime(df['index'], format='%b/%y') 
df = df.set_index('index')

def prepare_arima_data(data): 
    data = data.dropna() 
    return data

#Função para ajustar o modelo ARIMA 
def arima_forecast(data, order, steps): 
    data = prepare_arima_data(data) 
    model = ARIMA(data, order=order) 
    model_fit = model.fit() 
     
    #Fazer previsões 
    forecast = model_fit.forecast(steps=steps) 
     
    return forecast, model_fit
 
#Função para ajustar o modelo SARIMA 
def sarima_forecast(data, order, seasonal_order, steps): 
    data = prepare_arima_data(data) 
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order) 
    model_fit = model.fit(disp=False) 
     
    #Fazer previsões 
    forecast = model_fit.forecast(steps=steps) 
     
    return forecast, model_fit 

#Parâmetros dos modelos 
p, d, q = 1, 1, 1  #Ordem do modelo ARIMA 
P, D, Q, s = 1, 1, 1, 12  #Ordem sazonal do modelo SARIMA antes do ajuste 
#P, D, Q, s = 1, 0, 2, 12  #Ordem sazonal do modelo SARIMA depois do ajuste 
 
#Dicionário para meses 
meses_portugues = { 
    'Jan': 'Jan', 'Feb': 'Fev', 'Mar': 'Mar', 'Apr': 'Abr', 'May': 'Mai', 'Jun': 'Jun', 
    'Jul': 'Jul', 'Aug': 'Ago', 'Sep': 'Set', 'Oct': 'Out', 'Nov': 'Nov', 'Dec': 'Dez' 
} 
 
def formatar_mes_portugues(date): 
    mes = date.strftime('%b') 
    ano = date.strftime('%y') 
    return f'{meses_portugues[mes]}/{ano}' 
 
#Função para calcular RMSE 
def calculate_rmse(real, predicted): 
    return np.sqrt(mean_squared_error(real, predicted)) 

#Prever para cada hortaliça 
forecasts_arima = {} 
forecasts_sarima = {} 
rmse_arima = {} 
rmse_sarima = {} 
horticolas = df.columns[1:]  
 
for hort in horticolas: 
    if df[hort].dtypes != 'float64': 
        df[hort] = df[hort].str.replace(',', '.') 
        df[hort] = pd.to_numeric(df[hort], errors='coerce') 
     
    arima_predictions = [None] * len(df) 
    sarima_predictions = [None] * len(df) 
     
    #Fazer previsões para cada ponto no tempo a partir do mês 30 
    for i in range(30, len(df)): 
        data = df[hort][:i+1] 
        forecast_arima, _ = arima_forecast(data, order=(p, d, q), steps=1) 
        forecast_sarima, _ = sarima_forecast(data, order=(p, d, q), seasonal_order=(P, D, Q, s), steps=
 1) 
         
        arima_predictions[i] = forecast_arima.iloc[0] 
        sarima_predictions[i] = forecast_sarima.iloc[0] 
     
    #Prever mais três meses à frente 
    final_data = df[hort] 
    forecast_arima_next_3, _ = arima_forecast(final_data, order=(p, d, q), steps=3) 
    forecast_sarima_next_3, _ = sarima_forecast(final_data, order=(p, d, q), seasonal_order=(P, D, Q, s
 ), steps=3) 
     
    forecasts_arima[hort] = arima_predictions + list(forecast_arima_next_3) 
    forecasts_sarima[hort] = sarima_predictions + list(forecast_sarima_next_3) 
     
    #Calcular RMSE 
    rmse_arima[hort] = calculate_rmse(df[hort][30:], arima_predictions[30:]) 
    rmse_sarima[hort] = calculate_rmse(df[hort][30:], sarima_predictions[30:]) 

#Criar um novo dataframe para armazenar as previsões 
horticolas_dfs = {} 
for hort in horticolas: 
    extended_dates = list(df.index.strftime('%b/%y')) + [formatar_mes_portugues(df.index[
1] + pd.DateOffset(months=i)) for i in range(1, 4)] 
    hort_df = pd.DataFrame({ 
        'Meses': extended_dates, 
        'Dados Reais': list(df[hort]) + [None, None, None], 
        'ARIMA': forecasts_arima[hort], 
        'SARIMA': forecasts_sarima[hort] 
    }) 
    horticolas_dfs[hort] = hort_df 
 
#Imprimir os dataframes e RMSE para cada hortaliça 
for hort, hort_df in horticolas_dfs.items(): 
    print(f'Hortaliça: {hort}') 
    print(hort_df) 
    print(f'RMSE ARIMA: {rmse_arima[hort]}') 
    print(f'RMSE SARIMA: {rmse_sarima[hort]}') 
 
#Salvar os dataframes 
with pd.ExcelWriter('Previsoes_Horticolas_02.xlsx') as writer: 
    for hort, hort_df in horticolas_dfs.items(): 
        hort_df.to_excel(writer, sheet_name=hort, index=False) 