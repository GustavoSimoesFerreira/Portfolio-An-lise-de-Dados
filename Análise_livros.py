import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('vendas_livros.csv')   # Valores inventados

# Mostra as primeiras cinco linhas do dataset
print(df.head(5))



######## Explorando Dados ########

# Informações gerais sobre o dataframe
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Verifica valores ausentes
print(df.isnull().sum())



######## Análise Exploratória ########

# Adiciona uma coluna de receita
df['receita'] = df['preco'] * df['quantidade']

# Total de receita por autor
total_receita_autor = df.groupby('autor')['receita'].sum().sort_values(ascending=False)
print(total_receita_autor)

# Visualização de receita por autor
plt.figure(figsize=(10, 6))
sns.barplot(x=total_receita_autor.index, y=total_receita_autor.values, palette='viridis')
plt.title('Receita Total por Autor', fontsize=16)
plt.xlabel('Autor', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



######## Análise Temporal ########

# Converte a coluna de data para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Agrupa por mês e calcular receita total
df['mes'] = df['data_venda'].dt.to_period('M')
vendas_mensais = df.groupby('mes')['receita'].sum()

# Visualização das vendas mensais
plt.figure(figsize=(12, 6))
plt.plot(vendas_mensais.index.to_timestamp(), vendas_mensais.values, marker='o', color='b', linestyle='-', linewidth=2)
plt.title('Receita Mensal de Vendas', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Formata o eixo x para exibir melhor as datas
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator())
plt.gcf().autofmt_xdate()  # Rotaciona as datas

plt.tight_layout()
plt.show()
