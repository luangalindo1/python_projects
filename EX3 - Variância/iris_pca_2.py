import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Carregando o dataset para um arquivo dataframe
df = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])


# Inicialmente é necessário normalizar os dados

features = ['sepal length', 'sepal width', 'petal length', 'petal width']

# Separando os atributos
x = df.loc[:, features].values

# Separando as classes (variável objetivo)
y = df.loc[:,['target']].values

# Normalizando os atributos
x = StandardScaler().fit_transform(x)

# Calcular a PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

print(pca.explained_variance_ratio_)
print(pca.components_)

print(sum(pca.components_[0,:]*x[0,:])) #(coluna das componentes) x (linha das variáveis)
print(sum(pca.components_[1,:]*x[0,:]))


principalDf = pd.DataFrame(data = principalComponents
                           , columns = ['Componente principal 1', 'Componente principal 2'])

finalDf = pd.concat([principalDf, df[['target']]], axis = 1)


# Visualizar os dados em duas dimensões
import matplotlib.pyplot as plt


fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Componente principal 1', fontsize = 15)
ax.set_ylabel('Componente principal 2', fontsize = 15)
ax.set_title('2 componentes PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'Componente principal 1']
               , finalDf.loc[indicesToKeep, 'Componente principal 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.show()

