# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 08:39:06 2022

@author: LAT
"""

import pandas as pd
import numpy as np
from statistics import variance

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length',
                             'petal width', 'target'])

feature = ['sepal length', 'sepal width', 'petal length', 'petal width']

x = df.loc[:, feature].values

y = df.loc[:, ['target']].values

sl = x[:,0]
sw = x[:,1]
pl = x[:,2]
pw = x[:,3]

variancia = np.array([variance(sl), variance(sw), variance(pl),
                     variance(pw)])

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('sepal length', fontsize=15)
ax.set_ylabel('petal length', fontsize=15)
ax.set_title('representação em 2D', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = df['target'] == target
    ax.scatter(df.loc[indicesToKeep, 'sepal length'],
               df.loc[indicesToKeep, 'petal length'],
               c = color,
               s = 50)
ax.legend(targets)
ax.grid()
plt.show()