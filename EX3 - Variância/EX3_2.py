# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:19:18 2022

@author: LAT
"""

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length',
                             'petal width', 'target'])

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
target = label_encoder.fit_transform(df['target'])
target = pd.DataFrame(target, columns=['target'])

base = df.iloc[:, 0:4]
base = pd.concat([base, target], axis=1)

correlacao = base.corr()

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('sepal length', fontsize=15)
ax.set_ylabel('petal width', fontsize=15)
ax.set_title('representação em 2D', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = df['target'] == target
    ax.scatter(df.loc[indicesToKeep, 'sepal length'],
               df.loc[indicesToKeep, 'petal width'],
               c = color,
               s = 50)
ax.legend(targets)
ax.grid()
plt.show()