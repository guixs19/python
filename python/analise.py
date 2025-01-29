import pandas as pd
import matplotlib.pyplot as plt

dados=pd.read_csv("dados_vendas.csv")
print(dados.head())  #printar as primeiras colunas
print(dados.info())
#exibir informações dos dados
print(dados.isnull().sum())
#verificar valores ausentes
dados=dados.dropna()
#remover linhas com valores ausentes
#criação de grafico:
dados.groupby('produto')['vendas'].sum().plot(kind='bar',color='skyblue')
plt.title('Vendas por Produtos')
plt.xlabel('Produtos')
plt.ylabel('Total de Vendas')
plt.show()
dados['data']=pd.to_datetime(dados['data'])
#grafico de linha de vendas conforme o Tempo
dados.groupby('data')
['vendas'].sum().ploat(kind='line',color='green')
plt.title('Vendas ao Longo do Tempo')
plt.xlabel('data')
plt.ylabel('vendas')
plt.show()

