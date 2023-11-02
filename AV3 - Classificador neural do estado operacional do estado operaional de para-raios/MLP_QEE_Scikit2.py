# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:30:03 2020

@author: georg


Luan Fabio Marinho Galindo

118 110 382
"""
#from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
#from sklearn.metrics import plot_confusion_matrix # meu compilador não carregou
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#caso seja necessário
#pip install scikit-plot
#pip install sklearn
import scikitplot as skplt

import matplotlib.pyplot as plt

# pip install pandas
import pandas as pd


# carrega a base de dados
corrente1 = pd.read_csv("corrente_PR_BOM.csv", sep=",", header=None)
corrente0 = pd.read_csv("corrente_PR_DEF.csv", sep=",", header=None)
tensao1 = pd.read_csv("tensao_PR_BOM.csv", sep=",", header=None)
tensao0 = pd.read_csv("tensao_PR_DEF.csv", sep=",", header=None)
tempo1 = pd.read_csv("tempo_PR_BOM.csv", sep=",", header=None)
tempo0 = pd.read_csv("tempo_PR_DEF.csv", sep=",", header=None)


# análise inicial
plt.plot(corrente1.iloc[0, 7:])
plt.plot(corrente1.iloc[0, :7])

#por inspeção, determinou-se o intervalo de erros de medição
#e percebeu-se que este é igual em todas as medições
#assim, iremos remover os erros

corrente1.drop(range(0,8), axis=1, inplace=True)
plt.plot(corrente1.iloc[0, :])

corrente0.drop(range(0,8), axis=1, inplace=True)
tensao1.drop(range(0,8), axis=1, inplace=True)
tensao0.drop(range(0,8), axis=1, inplace=True)

#fazendo o downsampling para 200 amostras
from scipy.signal import decimate

amostras = 200

tempo0 = decimate(tempo0, int(len(tempo0.iloc[0,:])/amostras)) 
tempo1 = decimate(tempo1, int(len(tempo1.iloc[0,:])/amostras))

aux = decimate(corrente0, int(len(corrente0.iloc[0, :])/amostras))
corrente0 = pd.DataFrame(aux)

aux = decimate(corrente1, int(len(corrente1.iloc[0, :])/amostras))
corrente1 = pd.DataFrame(aux)

aux = decimate(tensao0, int(len(tensao0.iloc[0, :])/amostras))
tensao0 = pd.DataFrame(aux)

aux = decimate(tensao1, int(len(tensao1.iloc[0, :])/amostras))
tensao1 = pd.DataFrame(aux)

#realizando o drop das ultimas colunas
corrente0.drop(range(200,204), axis=1, inplace=True)
corrente1.drop(200, axis=1, inplace=True)
tensao0.drop(range(200,204), axis=1, inplace=True)
tensao1.drop(200, axis=1, inplace=True)


#concatenando os dados
corrente = pd.concat([corrente0, corrente1], ignore_index=1)
tensao = pd.concat([tensao0, tensao1], ignore_index=1)
alvos = pd.DataFrame({'Saída': [0]*40 + [1]*40})

# Crias as bases de treinamento e teste
Ent_tre1, Ent_test1, Alvo_tre1, Alvo_test1 = train_test_split(corrente, alvos, 
                                                          test_size=0.3, random_state=50,
                                                          stratify=alvos)

Ent_tre2, Ent_test2, Alvo_tre2, Alvo_test2 = train_test_split(tensao, alvos, 
                                                          test_size=0.3, random_state=50,
                                                          stratify=alvos)

# Cria o modelo neural (uma camada oculta com 4 neurônios)
net = MLPClassifier(solver='lbfgs', max_iter=500, hidden_layer_sizes=(64), verbose=True, 
                    early_stopping=True, activation='tanh')

# Ajusta o modelo a partir da base de dados de treinamento
modelo_ajustado1 = net.fit(Ent_tre1, Alvo_tre1)
modelo_ajustado2 = net.fit(Ent_tre2, Alvo_tre2)

# Estima a precisão do modelo a partir da base de teste
score1 = modelo_ajustado1.score(Ent_test1, Alvo_test1)
print(score1)
score2 = modelo_ajustado2.score(Ent_test2, Alvo_test2)
print(score2)

# Calcula as previsões do modelo a partir da base de teste
previsoes1 = modelo_ajustado1.predict(Ent_test1)
prevpb1 = modelo_ajustado1.predict_proba(Ent_test1)

previsoes2 = modelo_ajustado2.predict(Ent_test2)
prevpb2 = modelo_ajustado2.predict_proba(Ent_test2)

acuracia1 = accuracy_score(Alvo_test1, previsoes1)
print(acuracia1)

acuracia2 = accuracy_score(Alvo_test2, previsoes2)
print(acuracia2)


print(classification_report(Alvo_test1, previsoes1))
print(classification_report(Alvo_test2, previsoes2))

# Calcula a matriz de confusão - diagonal principal são
# padrões estimados corretamente
confusao1 = confusion_matrix(Alvo_test1, previsoes1)
print(confusao1)

confusao2 = confusion_matrix(Alvo_test2, previsoes2)
print(confusao2)


# plota Matriz de Confusão
#opcoes_titulos = [("Matriz de confusão sem normalização", None),
#                  ("Matriz de confusão normalizada", 'true')]
#for titulo, norm in opcoes_titulos:
#    disp = plot_confusion_matrix(modelo_ajustado1, Ent_test1, 
#                                 Alvo_test1.values,
#                                 cmap=plt.cm.Blues,
#                                 normalize=norm)
#    disp.ax_.set_title(titulo)

#    print(titulo)
#    print(disp.confusion_matrix)

#plt.show()

# plota utilizando a biblioteca scikitplot
skplt.metrics.plot_confusion_matrix(Alvo_test1, previsoes1)
plt.show()

skplt.metrics.plot_confusion_matrix(Alvo_test2, previsoes2)
plt.show()

#plotar a ROC
skplt.metrics.plot_roc(Alvo_test1, prevpb1)
plt.show()

skplt.metrics.plot_roc(Alvo_test2, prevpb2)
plt.show()

#plotar precision recall
skplt.metrics.plot_precision_recall(Alvo_test1, prevpb1)
plt.show()

skplt.metrics.plot_precision_recall(Alvo_test2, prevpb2)
plt.show()

