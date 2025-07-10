import pandas as pd 
import matplotlib.pyplot as plt 

dados = pd.read_excel('Precos-Medio-Nampula-Cidade-2019-2024.xlsx', sheet_name='Preparados') 
dados.set_index('Designacao', inplace=True) 

plt.figure(figsize=(16, 10)) 
for item in dados.index: 
    plt.plot(dados.columns, dados.loc[item], label=item, marker='o') 

plt.title('Evolução dos Preços das Hortaliças', fontsize=20, weight='bold')  
plt.xlabel('Tempo', fontsize=14)   
plt.ylabel('Preço (em Meticais)', fontsize=14)   
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fontsize=12)   
plt.xticks(rotation=45, ha='right')   
plt.grid(True, linestyle='--', alpha=0.7)   
plt.tight_layout()

plt.show()