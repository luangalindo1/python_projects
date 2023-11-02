# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:30:03 2020

@author: georg
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#caso seja necessário instalar o scikit-plot
# pip install scikit-plot
import scikitplot as skplt

import matplotlib.pyplot as plt

import pandas as pd


# carrega a base de dados
iris = load_iris()
entradas = iris.data
alvos = iris.target
nomes_das_classes = iris.target_names

# Crias as bases de treinamento e teste
Ent_tre, Ent_test, Alvo_tre, Alvo_test = train_test_split(entradas, alvos, 
                                                          test_size=0.2, random_state=50,
                                                          stratify=alvos)

Alvo_tre_df = pd.DataFrame(Alvo_tre, columns = ['tipo_flor'])
Alvo_tre_df.groupby(['tipo_flor']).size()


# Cria o modelo neural (uma camada oculta com 4 neurônios)
net = MLPClassifier(solver='lbfgs', max_iter=500, hidden_layer_sizes=(4), verbose=True, 
                    early_stopping=True, activation='tanh')

# Ajusta o modelo a partir da base de dados de treinamento
modelo_ajustado = net.fit(Ent_tre, Alvo_tre)

# Estima a precisão do modelo a partir da base de teste
score = modelo_ajustado.score(Ent_test, Alvo_test)
print(score)

# Calcula as previsões do modelo a partir da base de teste
previsoes = modelo_ajustado.predict(Ent_test)
prevpb = modelo_ajustado.predict_proba(Ent_test)

acuracia = accuracy_score(Alvo_test, previsoes)
print(acuracia)

print(classification_report(Alvo_test, previsoes))

# Calcula a matriz de confusão - diagonal principal são
# padrões estimados corretamente
confusao = confusion_matrix(Alvo_test, previsoes)
print(confusao)

# plota Matriz de Confusão
opcoes_titulos = [("Matriz de confusão sem normalização", None),
                  ("Matriz de confusão normalizada", 'true')]
for titulo, norm in opcoes_titulos:
    disp = plot_confusion_matrix(modelo_ajustado, Ent_test, 
                                 Alvo_test.values,
                                 display_labels=nomes_das_classes,
                                 cmap=plt.cm.Blues,
                                 normalize=norm)
    disp.ax_.set_title(titulo)

    print(titulo)
    print(disp.confusion_matrix)

plt.show()

# plota utilizando a biblioteca scikitplot
skplt.metrics.plot_confusion_matrix(Alvo_test, previsoes)
plt.show()

#plotar a ROC
skplt.metrics.plot_roc(Alvo_test, prevpb)
plt.show()

skplt.metrics.plot_precision_recall(Alvo_test, prevpb)
plt.show()



