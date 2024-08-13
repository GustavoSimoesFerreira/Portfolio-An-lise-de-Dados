import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Carregar os dados
df = pd.read_csv('vendas_livros.csv')   # Valores inventados

# Mostrar as primeiras linhas do dataset
print(df.head(5))



######## Explorando Dados ########

# Informações gerais sobre o dataframe
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Verificar valores ausentes
print(df.isnull().sum())



######## Análise Exploratória ########

# Adicionar uma coluna de receita
df['receita'] = df['preco'] * df['quantidade']

# Total de receita por autor
total_receita_autor = df.groupby('autor')['receita'].sum().sort_values(ascending=False)
print(total_receita_autor)

# Visualização de receita por autor
plt.figure(figsize=(10, 6))
sns.barplot(x=total_receita_autor.index, y=total_receita_autor.values, palette='viridis')
plt.title('Receita Total por Autor')
plt.xlabel('Autor')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.show()



######## Análise Temporal ########

# Converter a coluna de data para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Agrupar por mês e calcular receita total
df['mes'] = df['data_venda'].dt.to_period('M')
vendas_mensais = df.groupby('mes')['receita'].sum()

# Visualização das vendas mensais
plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o', color='b')
plt.title('Receita Mensal de Vendas')
plt.xlabel('Mês')
plt.ylabel('Receita')
plt.grid(True)
plt.show()
