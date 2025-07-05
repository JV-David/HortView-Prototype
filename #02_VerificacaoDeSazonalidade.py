import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.seasonal import seasonal_decompose 

dados = pd.read_excel('Precos-Medio-Nampula-Cidade-2019-2024.xlsx', sheet_name='PGrafico') 
dados.set_index('Designacao', inplace=True) 

resultados = [] 
#Iterar sobre cada hortaliça e realizar a decomposição sazonal 
for item in dados.index: 
    serie_temporal = dados.loc[item].copy() 
    serie_temporal.index = pd.to_datetime(serie_temporal.index)  
    decomposicao = seasonal_decompose(serie_temporal, model='additive', period=12)  
    resultados.append(decomposicao)

#Plotar os resultados da decomposição sazonal 
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 8)) 
fig.suptitle('Decomposição Sazonal dos Preços das Hortaliças', fontsize=16, weight='bold')

#Definir as linhas e colunas para cada subgráfico 
linhas = [0, 0, 1, 1] 
colunas = [0, 1, 0, 1] 
for i, item in enumerate(dados.index[:4]):  
    axes[linhas[i], colunas[i]].plot(resultados[i].observed, label='Observado') 
    axes[linhas[i], colunas[i]].plot(resultados[i].trend, label='Tendência') 
    axes[linhas[i], colunas[i]].plot(resultados[i].seasonal, label='Sazonalidade') 
    axes[linhas[i], colunas[i]].plot(resultados[i].resid, label='Resíduos') 
    axes[linhas[i], colunas[i]].set_title(item) 
    axes[linhas[i], colunas[i]].legend() 
    axes[linhas[i], colunas[i]].grid(True, linestyle='--', alpha=0.5) 
plt.tight_layout() 
plt.show() 