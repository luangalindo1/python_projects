# Luan Fabio Marinho Galindo
# 118 110 382

import numpy as np

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
                #print("Erro:", erro, ", na epoca:", n_epoca)
                self.pesos[1:] += self.taxa_aprendizagem * erro * entradas
                self.pesos[0] += self.taxa_aprendizagem * erro
                erro_total = erro_total + erro
                #print(erro_total)
            if abs(erro_total/i) <= 10e-4:
                break
           
                              
#utilizacao 

#entradas boleanas    
entradas_treino = []
entradas_treino.append(np.array([1, 1]))
entradas_treino.append(np.array([1, 0]))
entradas_treino.append(np.array([0, 1]))
entradas_treino.append(np.array([0, 0]))

#saida OR
alvos = np.array([1, 1, 1, 0])

perceptron = Perceptron(2, 20, 0.1) #informamos apenas o número de entradas (duas), os
#demais parâmetros ficaram com valores padrão
perceptron.treinar(entradas_treino, alvos)

entrada_teste = np.array([1, 1])
saida_teste1 = perceptron.calc_saida(entrada_teste) 
print("Saída1: ", saida_teste1)
# => 1

entrada_teste = np.array([0, 0])
saida_teste2 = perceptron.calc_saida(entrada_teste) 
print("Saída2: ", saida_teste2)
# => 0                