# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:10:52 2022

@author: luanfabiomg
"""

# importação das bibliotecas

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from math import ceil
from scipy import stats 
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt
import seaborn as srn

#------------------------------------------------------------------------------
# amostragem simples

# carregamento dos dados
base = pd.read_csv('iris2.csv')
print(base.head())

# verificar tamanho da base de dados
print(base.shape)

# mudança na semente aleatória para manter os resultados em várias execuções
np.random.seed(3000) # o argumento é o número de "partida" do gerador

# escolha aleatória de 150 amostras
amostra = np.random.choice(a = [0, 1], size = 150, replace=True, 
                           p = [0.7, 0.3]) # p é a proporção

# verificar tamanho da amostra
print(len(amostra))

# verificar valores específicos da amostra
print(len(amostra[amostra == 1]))
print(len(amostra[amostra == 0]))

print(amostra)

# geração de nova base de dados com base num valor da amostra
base_trein = base.loc[amostra[amostra == 0]]
print(base_trein.shape)
base_teste = base.loc[amostra[amostra == 1]]
print(base_teste.shape)

# amostragem estratificada
print(base['class'].value_counts())

X, _, y, _ = train_test_split(base.iloc[:, 0:4], base.iloc[:, 4], #sklearn
                              test_size = 0.3, stratify = base.iloc[:, 4])
                                        # a estratificação não deixa o modelo enviesado
# sem considerar estratificação
#X, _, y, _ = train_test_split(base.iloc[:, 0:4], base.iloc[:, 4],
#                             test_size = 0.3)

print(y.value_counts())

# carregamento de base de dados desbalanceada
infert = pd.read_csv('infert.csv')
print(infert.head())

# contagem de registro considerando o atributo "educação"
print(infert['education'].value_counts())

# criando uma amostra com 40% dos registros
X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[0:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1]) #corrigir

# sem estratificação
#X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[0:, 1],
#                              test_size = 0.6)

print(y1.value_counts())

# amostragem sistemática

# criação das variáveis

tam_popolacao = 150     # base IRIS
tam_amostra = 15        # instâncias que serão amostradas
espa = ceil(tam_popolacao/tam_amostra) # espaçamento
print(espa)

# definição de valor randômico para inicializar o vetor de estolhidos
r_esco = np.random.randint(low = 1, high = espa + 1, size = 1)
print(r_esco)

# soma
acumulador = r_esco[0]
sorteados = []
for i in range(tam_amostra):
    sorteados.append(acumulador)
    acumulador += espa
print(sorteados)
print(len(sorteados))

# criação de nova base de dados
base = pd.read_csv('iris2.csv')
base_final = base.loc[sorteados]
print(base_final)

# metricas de centralidade e variabilidade

# criação de variáveis com salários
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

print(np.mean(jogadores))
print(np.median(jogadores))

# variável para geração de quartis
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1]) #50% equivale a mediana
print(quartis)

# desvio padrão
print(np.std(jogadores, ddof = 1))

# estatísticas detalhadas com scipy
# simetria: moda, mediana e media iguais (A = 0)
# A: coeficiente de pearson - refere-se a simetria também
# curtose: achatamento da curva
stats.describe(jogadores)
srn.displot(x = jogadores, kde=True)

# distribuição normal
# media 8, dp 2, valor < 6 
norm.cdf(6, 8, 2)

# função de sobrevivência ou confiabilidade
norm.sf(6, 8, 2) # ou 1 - norm.cdf(6, 8, 2)

# probabilidade de valor < 6 ou valor > 10
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

# probablidade de valor < 10 e valor > 8
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)


# verificação da distribuição normal

# variável com dados em distribuição normal
dados = norm.rvs(size = 1000)
stats.describe(dados)
print(dados)

# histograma
plt.hist(dados, bins = 20)
plt.title('Dados')

# Geração de gráfico para verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados, fit=True, plot=ax)
plt.show()

# teste de shapiro
stats.shapiro(dados)

# simulando distribuições assimetricas
dados2 = skewnorm.rvs(5, size=1000) # assimetria positiva
stats.describe(dados2)

# histograma
plt.hist(dados2, bins = 20)
plt.title('Dados')

# verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados2, fit=True, plot=ax)
plt.show()

stats.shapiro(dados2)

dados3 = skewnorm.rvs(-5, size=1000) # assimetria negativa
stats.describe(dados3)

# histograma
plt.hist(dados3, bins = 20)
plt.title('Dados3')

# verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados3, fit=True, plot=ax)
plt.show()

stats.shapiro(dados3)
