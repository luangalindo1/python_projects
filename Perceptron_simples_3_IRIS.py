# Luan Fabio Marinho Galindo
# 118 110 382
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    #URL_='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    #dados = pd.read_csv(URL_, header = None)
    dados = pd.read_csv("iris.csv", sep=",", header = None)
    print(dados)
    
    #Seleciona-se apenas os 100 primeiros pontos, os quais correspodem as classes
    #Setosa e Versicolor (as classes linearmente separaveis)
    dadosls = dados[:100]
    #substitui, na última coluna, o label Iris-setosa por 0 e Iris-Versicolor por 1 
    #visando a classificação binária
    dadosls[4] = np.where(dadosls.iloc[:, -1]=='Iris-setosa', 0, 1)
    dadosls = np.asmatrix(dadosls, dtype = 'float64')
    return dadosls

class Perceptron(object):

    def __init__(self, num_entradas, epocas=20, taxa_aprendizagem=0.1):
        self.epocas = epocas
        self.taxa_aprendizagem = taxa_aprendizagem
        self.pesos = 10e-4*np.random.uniform(low=0, high=1, size=(num_entradas + 1)) #mais 01 do bias
                    #gerando pesos aleatórios
    def calc_saida(self, entradas):
        net = np.dot(entradas, self.pesos[1:]) + self.pesos[0]
        if net > 0:
          saida = 1
        else:
          saida = 0            
        return saida

    def treinar(self, entradas_treino, alvos):
        n_epoca = 0
        for _ in range(self.epocas):
            n_epoca = n_epoca + 1
            erro = 0
            i = 0
            erro_total = 0
            for entradas, alvo in zip(entradas_treino, alvos):
                i = i+1
                estimacao = self.calc_saida(entradas)
                erro = alvo - estimacao
                #atualiza os pesos transformando os dados no formato matriz para array
                self.pesos[1:] += np.squeeze(np.asarray(self.taxa_aprendizagem * erro * entradas))
                self.pesos[0] += self.taxa_aprendizagem * erro
                erro_total = erro_total + erro
                #print("ERRO TOTAL", erro_total)
            if abs(erro_total/i) <= 10e-4:
                break #parando o processo caso o erro seja mínimo
                

#CODIGO PRINCIPAL

basedados = load_data()

dados_rand = np.random.permutation(basedados)
#Composicao dos dados
'''
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa: 50 primeiros elementos
-- Iris Versicolour: 50 elementos intermediários
-- Iris Virginica: 50 elementos finais
'''

plt.scatter(np.array(basedados[:50,0]), np.array(basedados[:50,2]), marker='o', label='setosa')
plt.scatter(np.array(basedados[50:,0]), np.array(basedados[50:,2]), marker='x', label='versicolor')
plt.xlabel('Comprimento da pétala')
plt.ylabel('Comprimento da sépala')
plt.legend()
plt.show()

                              
#utilizacao 

#entradas para treinamento    
entradas_treino = dados_rand[:70, :-1] # todos os dados exceto o label

#saida para treinamento
alvos = dados_rand[70:, -1] #seleciona apenas última coluna - o label

perceptron = Perceptron(4) #informamos apenas o número de entradas (quatro), os
#demais parâmetros ficarão com valores padrão
perceptron.treinar(entradas_treino, alvos)

#acerto = 0
#erro = 0
#for linha in range(70):
#    if perceptron.calc_saida(entradas_treino[:linha,:]) == 1:
#       acerto +=1
#    else:
#       erro +=1
#print("A taxa de acerto é: ", acerto/(erro + acerto))

#setosa
entrada_teste = np.array([5.1, 3.5, 1.4, 0.2])
saida_teste1 = perceptron.calc_saida(entrada_teste) 
print("Saída 1: ", saida_teste1)

#Versicolor
entrada_teste = np.array([7, 3.2, 4.5, 1.4])
saida_teste2 = perceptron.calc_saida(entrada_teste) 
print("Saída 2: ", saida_teste2)

#Virginica 
entrada_teste = np.array([6.3, 3.3, 6, 2.5])
saida_teste3 = perceptron.calc_saida(entrada_teste) 
print("Saída 3: ", saida_teste3)